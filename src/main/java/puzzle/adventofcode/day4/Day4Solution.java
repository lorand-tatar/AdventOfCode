package puzzle.adventofcode.day4;

import static java.nio.file.Files.readAllLines;
import static java.util.stream.Collectors.toList;

import java.io.IOException;
import java.nio.file.Path;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Comparator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import puzzle.adventofcode.Solution;

public class Day4Solution implements Solution {

    private Comparator<LogEntry> logComparator = LogComparator.INSTANCE;

    @Override
    public void run() {
        try {
            var rawSystemLogs = readAllLines(Path.of("C:/Users/Flori/IdeaProjects/AdventOfCode/src/main/resources/puzzle4a_input.txt"));
            var logEntriesInOrder = rawSystemLogs.stream()
                    .map(this::convertToLogEntry)
                    .sorted(logComparator)
                    .collect(toList());
            logEntriesInOrder.stream().limit(10).forEach(System.out::println);

        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }

    }

    private LogEntry convertToLogEntry(String rawLogEntry) {
        String[] entryParts = rawLogEntry.split("\\]\\s");
        var entry = new LogEntry(LocalDateTime.parse(entryParts[0].substring(1), DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")),
                MessageType.parse(entryParts[1]),
                extractGuardId(entryParts[1]));
        return entry;
    }

    private Integer extractGuardId(String message) {
        var idMatcher = Pattern.compile(".*#(\\d)+.*").matcher(message);
        return idMatcher.matches() ? Integer.valueOf(idMatcher.group(1)) : null;
    }
}
