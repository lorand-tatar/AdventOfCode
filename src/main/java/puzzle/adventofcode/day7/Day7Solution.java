package puzzle.adventofcode.day7;

import puzzle.adventofcode.Solution;

import java.io.IOException;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static java.nio.file.Files.readAllLines;
import static java.util.stream.Collectors.toList;

public class Day7Solution implements Solution {

    private static final Pattern INSTRUCTION_PATTERN = Pattern.compile("Step (\\w) must be finished before step (\\w) can begin\\.");

    @Override
    public void run() {
        try {
            var rawInstructions = readAllLines(Path.of("C:/Users/Flori/IdeaProjects/AdventOfCode/src/main/resources/puzzle7a_input.txt"));

            List<Prerequisite> prerequisites = rawInstructions.stream()
                    .map(instruction -> {
                        Matcher instructionMatcher = INSTRUCTION_PATTERN.matcher(instruction);
                        instructionMatcher.lookingAt();
                        return new Prerequisite(instructionMatcher.group(1).charAt(0), instructionMatcher.group(2).charAt(0));
                    })
                    .collect(toList());

            var graph = new TaskGraph(new HashSet<>());
            
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }
    }

    private class Prerequisite {
        private Character prerequisite;
        private Character ofThisOne;

        private Prerequisite(Character prerequisite, Character ofThisOne) {
            this.prerequisite = prerequisite;
            this.ofThisOne = ofThisOne;
        }

        private Character getPrerequisite() {
            return prerequisite;
        }

        private Character getOfThisOne() {
            return ofThisOne;
        }

        @Override
        public String toString() {
            return prerequisite + " before " + ofThisOne;
        }
    }
}
