package puzzle.adventofcode.day2;

import static java.nio.file.Files.readAllLines;

import java.io.IOException;
import java.nio.file.Path;
import java.util.IdentityHashMap;
import java.util.Map;
import java.util.Optional;

import puzzle.adventofcode.Solution;

public class Day2Solution implements Solution {
    private int numberOfExactlyTwoHolders = 0;
    private int numberOfExactlyThreeHolders = 0;

    @Override
    public void run() {
        try {
            var boxIds = readAllLines(Path.of("C:/stash/AdventOfCode/src/main/resources/puzzle2a_input.txt"));
            System.out.println("Box ids: " + boxIds + "\n, " + boxIds.size() + " of them");

            boxIds.stream().forEach(this::countOccurences);
            System.out.println(numberOfExactlyTwoHolders);
            System.out.println(numberOfExactlyThreeHolders);
            System.out.println("Checksum: " + numberOfExactlyTwoHolders * numberOfExactlyThreeHolders);

            for (String boxId1 : boxIds) {
                for (String boxId2 : boxIds) {
                    if (idDistance(boxId1, boxId2) == 1) {
                        System.out.println("The matching boxes: " + boxId1 + ", " + boxId2);
                        return;
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }

    }

    private Integer idDistance(String boxId1, String boxId2) {
        final char[] chars1 = boxId1.toCharArray();
        final char[] chars2 = boxId2.toCharArray();

        int distance = 0;
        for (int i = 0; i < chars1.length; ++i) {
            if (chars1[i] != chars2[i])
                distance++;
        }
        return distance;
    }

    private void countOccurences(String boxId) {
        var charOccurences = new IdentityHashMap<Character, Integer>();
        boxId.chars().mapToObj(c -> (char) c)
            .forEach(c -> increaseOccurence(c, charOccurences));
        charOccurences.entrySet().stream()
            .filter(entry -> entry.getValue() == 2)
            .findFirst().ifPresent(entry -> numberOfExactlyTwoHolders++);
        charOccurences.entrySet().stream()
            .filter(entry -> entry.getValue() == 3)
            .findFirst().ifPresent(entry -> numberOfExactlyThreeHolders++);
    }

    private void increaseOccurence(char c, Map<Character, Integer> occurenceMap) {
        final Integer previousOccurence = Optional.ofNullable(occurenceMap.get(c)).orElse(0);
        occurenceMap.put(c, previousOccurence + 1);
    }
}
