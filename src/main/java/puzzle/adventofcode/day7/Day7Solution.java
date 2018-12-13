package puzzle.adventofcode.day7;

import puzzle.adventofcode.Solution;
import puzzle.adventofcode.day7.TaskGraph.GraphNode;

import java.io.IOException;
import java.nio.file.Path;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import static java.lang.Boolean.FALSE;
import static java.lang.Boolean.TRUE;
import static java.nio.file.Files.readAllLines;
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;
import static java.util.stream.Collectors.toSet;

public class Day7Solution implements Solution {

    private static final Pattern INSTRUCTION_PATTERN = Pattern.compile("Step (\\w) must be finished before step (\\w) can begin\\.");
    private static final int WORKER_COUNT = 5;

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
            buildTaskGraph(prerequisites, graph);
            System.out.println(graph);
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
            var timeTick = 0;
            var workerBusiness = new HashMap<Integer, Boolean>();
            IntStream.range(0, WORKER_COUNT)
                    .mapToObj(workerId -> Map.entry(workerId, FALSE))
                    .forEach(entry -> workerBusiness.put(entry.getKey(), entry.getValue()));
            HashMap<Integer, GraphNode> workerAssignment = new HashMap<>();
            IntStream.range(0, WORKER_COUNT)
                    .mapToObj(workerId -> (Integer) workerId)
                    .forEach(workerId -> workerAssignment.put(workerId, null));
            while (workerBusiness.containsValue(TRUE) || !processableNodes.isEmpty()) {
                System.out.println("fresh start: " + processableNodes.stream().map(GraphNode::getTask).collect(toList()));
                if (workerBusiness.containsValue(FALSE)) {
                    var availableWorkers = workerBusiness.entrySet().stream()
                            .filter(entry -> !entry.getValue())
                            .collect(toList());
                    for (var worker : availableWorkers) {
                        workerAssignment.put(worker.getKey(), processableNodes.remove(0));
                        taskSequence = taskSequence.concat(String.valueOf(workerAssignment.get(worker.getKey()).getTask()));
                        workerBusiness.put(worker.getKey(), TRUE);
                    }
                }
                workerBusiness.entrySet().stream()
                        .filter(entry -> entry.getValue())
                        .forEach(entry -> workerAssignment.get(entry.getKey()).decreaseWorkTimeLeftByOneTick());
                List<GraphNode> finalProcessableNodes = processableNodes;
                workerAssignment.entrySet().stream()
                        .filter(entry -> entry.getValue().getTaskWorkTimeLeft() <= 0)
                        .forEach(entry -> {
                            doneSteps.add(entry.getValue());
                            finalProcessableNodes.addAll(entry.getValue().getFollowUps());
                            System.out.println("after inflate: " + finalProcessableNodes.stream().map(GraphNode::getTask).collect(toList()));
                            workerBusiness.put(entry.getKey(), FALSE);
                        });
                processableNodes = finalProcessableNodes;
                var intermediateSet = new HashSet<GraphNode>();
                intermediateSet.addAll(processableNodes);
                intermediateSet.removeAll(doneSteps);
                System.out.println("Making the list distinct and removed already done steps: " + intermediateSet.stream().map(GraphNode::getTask).collect(toSet()));
                intermediateSet.removeIf(node -> !doneSteps.containsAll(node.getDependencies()));
                System.out.println("Removed nodes that have incomplete dependencies: " + intermediateSet.stream().map(GraphNode::getTask).collect(toSet()));
                processableNodes = new ArrayList<GraphNode>(intermediateSet);
                processableNodes.sort(comparing(GraphNode::getTask));
                timeTick++;
            }
            System.out.println(taskSequence);
            System.out.println("done in " + timeTick + " ticks");
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
