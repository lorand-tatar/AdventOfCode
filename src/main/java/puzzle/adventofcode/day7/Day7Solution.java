package puzzle.adventofcode.day7;

import static java.nio.file.Files.readAllLines;
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import puzzle.adventofcode.Solution;
import puzzle.adventofcode.day7.TaskGraph.GraphNode;

public class Day7Solution implements Solution {

    private static final Pattern INSTRUCTION_PATTERN = Pattern.compile("Step (\\w) must be finished before step (\\w) can begin\\.");

    @Override
    public void run() {
        try {
            var rawInstructions = readAllLines(Path.of("C:/stash/AdventOfCode/src/main/resources/puzzle7a_input.txt"));

            List<Prerequisite> prerequisites = rawInstructions.stream()
                .map(instruction -> {
                    Matcher instructionMatcher = INSTRUCTION_PATTERN.matcher(instruction);
                    instructionMatcher.lookingAt();
                    return new Prerequisite(instructionMatcher.group(1).charAt(0), instructionMatcher.group(2).charAt(0));
                })
                .collect(toList());

            var graph = new TaskGraph(new HashSet<>());
            buildTaskGraph(prerequisites, graph);
            var startCandidates = graph.getNodes().stream()
                .filter(node -> node.getDependencies().isEmpty())
                .collect(toList());
            startCandidates.sort(comparing(GraphNode::getTask));
            var endNodes = graph.getNodes().stream()
                .filter(node -> node.getFollowUps().isEmpty())
                .collect(toList());
            // O P V starter, Q ending
            var processableNodes = startCandidates;
            var taskSequence = "";
            var doneSteps = new HashSet<GraphNode>();
            while (!processableNodes.isEmpty()) {
                final GraphNode expandedNode = processableNodes.get(0);
                taskSequence = taskSequence.concat(String.valueOf(expandedNode.getTask()));
                doneSteps.add(expandedNode);
                processableNodes.addAll(expandedNode.getFollowUps());
                System.out.println(processableNodes.size());
                var intermediateSet = new HashSet<GraphNode>();
                intermediateSet.addAll(processableNodes);
                intermediateSet.removeAll(doneSteps);
                System.out.println(processableNodes.size());
                processableNodes = new ArrayList<GraphNode>(intermediateSet);
                System.out.println(processableNodes.size());
                processableNodes.sort(comparing(GraphNode::getTask));
            }
            System.out.println(taskSequence);
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }
    }

    private void buildTaskGraph(List<Prerequisite> prerequisites, TaskGraph graph) {
        prerequisites.stream()
            .peek(prerequisite -> {
                var nodes = graph.getNodes();
                nodes.add(new GraphNode(prerequisite.getPrerequisite()));
                nodes.add(new GraphNode(prerequisite.getOfThisOne()));
            })
            .forEach(prerequisite -> {
                var leftNode = graph.lookUpNodeForTask(prerequisite.getPrerequisite());
                var rightNode = graph.lookUpNodeForTask(prerequisite.getOfThisOne());
                leftNode.addFollowUp(rightNode);
                rightNode.addDependency(leftNode);
            });
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
