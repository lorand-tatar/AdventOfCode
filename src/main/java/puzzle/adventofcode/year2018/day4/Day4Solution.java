package puzzle.adventofcode.year2018.day4;

import static java.lang.Math.toIntExact;
import static java.nio.file.Files.readAllLines;
import static java.time.LocalDateTime.now;
import static java.time.ZoneOffset.UTC;
import static java.time.temporal.ChronoUnit.MINUTES;
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;

import static puzzle.adventofcode.year2018.day4.MessageType.FALLS_ASLEEP;
import static puzzle.adventofcode.year2018.day4.MessageType.WAKES_UP;

import java.io.IOException;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import puzzle.adventofcode.Solution;

public class Day4Solution implements Solution {

    private Comparator<LogEntry> logComparator = LogComparator.INSTANCE;

    @Override
    public void run() {
        try {
            var rawSystemLogs = readAllLines(Path.of("C:/github/AdventOfCode/src/main/resources/puzzle4a_input.txt"));
            var logEntriesInOrder = rawSystemLogs.stream()
                .map(this::convertToLogEntry)
                .sorted(logComparator)
                .collect(toList());

            MessageType previousLogType = null;
            for (var logEntry : logEntriesInOrder) {
                if (FALLS_ASLEEP.equals(previousLogType) && logEntry.getMessage().equals(MessageType.BEGINS_SHIFT)) {
                    System.out.println("Damn, we have an unawaken guy before shift!");
                }
                previousLogType = logEntry.getMessage();
            }

            Map<Integer, Integer> asleepMinutes = setGuardIdsAndCountAsleepMinutes(logEntriesInOrder);
            System.out.println(asleepMinutes);

            Integer mostAsleepGuardId = asleepMinutes.entrySet().stream()
                .max(comparing(Map.Entry::getValue))
                .map(Map.Entry::getKey).orElseThrow();
            System.out.println("The guard that was the most minutes asleep: #" + mostAsleepGuardId);

            var favoriteSleepMinuteAndFrequency = determineFavoriteSleepMinute(logEntriesInOrder, mostAsleepGuardId);
            System.out.println("Favorite sleep minute of guard #" + mostAsleepGuardId + ": " + favoriteSleepMinuteAndFrequency.getKey());
            System.out.println("The product of the two numbers is: " + mostAsleepGuardId * favoriteSleepMinuteAndFrequency.getKey());

            Map.Entry<Integer, Map.Entry<Integer, Integer>> chosenGuardWithHisFavoriteMinuteToSleep = logEntriesInOrder.stream()
                .map(LogEntry::getGuardId)
                .distinct()
                .map(guardId -> {
                    return Map.entry(guardId, determineFavoriteSleepMinute(logEntriesInOrder, guardId));
                })
                .max(comparing(guardEntry -> guardEntry.getValue().getValue()))
                .orElseThrow();
            System.out.println("Guard #" + chosenGuardWithHisFavoriteMinuteToSleep.getKey() + " slept the most in minute " + chosenGuardWithHisFavoriteMinuteToSleep.getValue().getKey());
            System.out.println("The product of the two numbers is: " + chosenGuardWithHisFavoriteMinuteToSleep.getKey() * chosenGuardWithHisFavoriteMinuteToSleep.getValue().getKey());
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }

    }

    private Map.Entry<Integer, Integer> determineFavoriteSleepMinute(List<LogEntry> logEntriesInOrder, Integer mostAsleepGuardId) {
        List<LogEntry> mostAsleepGuardsLogs = logEntriesInOrder.stream()
            .filter(logEntry -> logEntry.getGuardId().equals(mostAsleepGuardId)).collect(toList());

        Map<Integer, Integer> howManyTimesAsleepInAMinute = new HashMap<>();
        LocalDateTime previousTimestamp = null;
        for (var logEntry : mostAsleepGuardsLogs) {
            if (logEntry.getMessage().equals(FALLS_ASLEEP)) {
                previousTimestamp = logEntry.getTimestamp();
            } else if (logEntry.getMessage().equals(WAKES_UP)) {
                IntStream.range(previousTimestamp.getMinute(), logEntry.getTimestamp().getMinute())
                    .forEach(minute -> {
                        var sleptCntInThatMinuteSoFar = Optional.ofNullable(howManyTimesAsleepInAMinute.get(minute)).orElse(0);
                        howManyTimesAsleepInAMinute.put(minute, sleptCntInThatMinuteSoFar + 1);
                    });
            }
        }

        return howManyTimesAsleepInAMinute.entrySet().stream()
            .max(comparing(Map.Entry::getValue))
            .orElse(Map.entry(-1, -1));
    }

    private Map<Integer, Integer> setGuardIdsAndCountAsleepMinutes(List<LogEntry> logEntriesInOrder) {
        Integer actualId = null;
        Map<Integer, Integer> asleepAmountPerGuard = new HashMap<>();
        // Whatever starting value, we trust the input to start with START_SHIFT entry first
        LocalDateTime eventTimestamp = now();
        for (var logEntry : logEntriesInOrder) {
            Integer guardId = logEntry.getGuardId();
            if (guardId != null) {
                actualId = guardId;
                eventTimestamp = logEntry.getTimestamp();
            } else {
                if (logEntry.getMessage().equals(WAKES_UP)) {
                    long asleepSoFar = Optional.ofNullable(asleepAmountPerGuard.get(actualId)).orElse(0);
                    // Based on the fact that one can only wake up after being asleep
                    asleepSoFar += MINUTES.between(eventTimestamp.atZone(UTC), logEntry.getTimestamp().atZone(UTC));
                    asleepAmountPerGuard.put(actualId, toIntExact(asleepSoFar));
                }

                eventTimestamp = logEntry.getTimestamp();

                logEntry.setGuardId(actualId);
            }
        }

        return asleepAmountPerGuard;
    }

    private LogEntry convertToLogEntry(String rawLogEntry) {
        String[] entryParts = rawLogEntry.split("\\]\\s");
        var entry = new LogEntry(LocalDateTime.parse(entryParts[0].substring(1), DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")),
            MessageType.parse(entryParts[1]),
            extractGuardId(entryParts[1]));
        return entry;
    }

    private Integer extractGuardId(String message) {
        var idMatcher = Pattern.compile(".*#(\\d+).*").matcher(message);
        return idMatcher.matches() ? Integer.valueOf(idMatcher.group(1)) : null;
    }
}
