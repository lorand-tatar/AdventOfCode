package puzzle.adventofcode.day5;

import puzzle.adventofcode.Solution;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Map;
import java.util.Set;

import static java.lang.Character.*;
import static java.nio.file.Files.readString;
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;
import static java.util.stream.Collectors.toSet;

public class Day5Solution implements Solution {

    @Override
    public void run() {
        try {
            var originalPolymer = readString(Path.of("C:/Users/Flori/IdeaProjects/AdventOfCode/src/main/resources/puzzle5a_input.txt"));

            System.out.println("The remaining polymer size: " + reducePolymer(originalPolymer));

            Set<Character> polymerBuildingBlocks = originalPolymer.chars()
                    .mapToObj(c -> (char) c)
                    .map(Character::toLowerCase)
                    .collect(toSet());
            Map.Entry<Character, Integer> charToRemoveForMinimalReduceLengthAndReducedLength = polymerBuildingBlocks.stream()
                    .map(buildingBlock -> Map.entry(buildingBlock,
                            originalPolymer
                                    .replace(String.valueOf(buildingBlock), "")
                                    .replace(String.valueOf(toUpperCase(buildingBlock)), "")))
                    .map(removedCharacterAndPolymer -> Map.entry(removedCharacterAndPolymer.getKey(),
                            reducePolymer(removedCharacterAndPolymer.getValue())))
                    .min(comparing(Map.Entry::getValue))
                    .orElseThrow();
            System.out.println("You should remove component " + charToRemoveForMinimalReduceLengthAndReducedLength.getKey() + ". Minimal achievable lenght is " + charToRemoveForMinimalReduceLengthAndReducedLength.getValue());
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }
    }

    private int reducePolymer(String originalPolymer) {
        Character previousChar = null;
        ArrayList<Character> previousIteration;
        ArrayList<Character> actualIteration = (ArrayList<Character>) originalPolymer.chars().mapToObj(c -> (char) c).collect(toList());
        do {
            previousIteration = new ArrayList<>(actualIteration);
            actualIteration = new ArrayList<>();
            var iterationCnt = 0;
            previousChar = null;
            var skipNext = false;
            for (var actualChar : previousIteration) {
                iterationCnt++;
                if (previousChar != null) {
                    if (!skipNext) {
                        if (!reacts(previousChar, actualChar)) {
                            actualIteration.add(previousChar);
                            if (iterationCnt == previousIteration.size()) {
                                actualIteration.add(actualChar);
                            }
                        } else {
                            skipNext = true;
                        }
                    } else {
                        if (iterationCnt == previousIteration.size()) {
                            actualIteration.add(actualChar);
                        }
                        skipNext = false;
                    }
                }
                previousChar = actualChar;
            }
        } while (previousIteration.size() != actualIteration.size());

        return actualIteration.size();
    }

    private boolean reacts(Character previousChar, Character actualChar) {
        return (toLowerCase(previousChar) == toLowerCase(actualChar)) &&
                ((isLowerCase(previousChar) && isUpperCase(actualChar)) ||
                        (isLowerCase(actualChar) && isUpperCase(previousChar)));
    }

}
