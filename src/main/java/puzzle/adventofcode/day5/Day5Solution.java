package puzzle.adventofcode.day5;

import puzzle.adventofcode.Solution;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.lang.Character.*;
import static java.nio.file.Files.readAllLines;
import static java.nio.file.Files.readString;
import static java.util.stream.Collectors.toList;

public class Day5Solution implements Solution {

    @Override
    public void run() {
        try {
            var originalPolymer = readString(Path.of("C:/Users/Flori/IdeaProjects/AdventOfCode/src/main/resources/puzzle5a_input.txt"));

            Character previousChar = null;
            int previousIterationSize;
            LinkedList<Character> nextIteration = originalPolymer.chars().mapToObj(c -> ((Character) c)).collect(toList())
            do {
                previousIterationSize = nextIteration.size();
                nextIteration = new LinkedList<>();
                char[] polymerChars = originalPolymer.toCharArray();
                for (var actualChar : polymerChars) {

                    var skipNext = false;
                    if (previousChar != null && !skipNext && !reacts(previousChar, actualChar)) {
                        nextIteration.add(previousChar);
                        if (polymerChars.indexOf(actualChar) = originalPolymer.)
                    } else {
                        skipNext = true;
                    }
                    previousChar = actualChar;
                }
            } while (previousIterationSize != nextIteration.size());

            System.out.println("The remaining polymer size: " + nextIteration.size());
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }
    }

    private boolean reacts(Character previousChar, Character actualChar) {
        return (toLowerCase(previousChar) == toLowerCase(actualChar)) &&
                ((isLowerCase(previousChar) && isUpperCase(actualChar)) ||
                        (isLowerCase(actualChar) && isUpperCase(previousChar)));
    }

}
