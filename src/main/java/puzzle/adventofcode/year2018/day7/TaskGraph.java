package puzzle.adventofcode.year2018.day7;

import static java.lang.Character.getNumericValue;
import static java.util.stream.Collectors.toList;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class TaskGraph {
    private Set<GraphNode> nodes;

    public TaskGraph(Set<GraphNode> nodes) {
        this.nodes = nodes;
    }

    public Set<GraphNode> getNodes() {
        return nodes;
    }

    public GraphNode lookUpNodeForTask(Character task) {
        return nodes.stream()
            .filter(node -> node.getTask().equals(task))
            .findFirst()
            .get();
    }

    @Override
    public String toString() {
        return "TaskGraph{" +
            "nodes=" + nodes +
            '}';
    }

    public static class GraphNode {
        private Character task;
        private Integer taskWorkTimeLeft;
        private Set<GraphNode> dependencies;
        private Set<GraphNode> followUps;

        public GraphNode(Character task) {
            this.task = task;
            taskWorkTimeLeft = 61 + getNumericValue(task) - getNumericValue('A');
            dependencies = new HashSet<>();
            followUps = new HashSet<>();
        }

        public GraphNode(Character task, Set<GraphNode> dependencies, Set<GraphNode> followUps) {
            this.task = task;
            taskWorkTimeLeft = 61 + getNumericValue(task) - getNumericValue('A');
            this.dependencies = dependencies;
            this.followUps = followUps;
        }

        public void addDependency(GraphNode dependency) {
            dependencies.add(dependency);
        }

        public void addFollowUp(GraphNode followUp) {
            followUps.add(followUp);
        }

        public void decreaseWorkTimeLeftByOneTick() {
            taskWorkTimeLeft--;
        }

        public Character getTask() {
            return task;
        }

        public Integer getTaskWorkTimeLeft() {
            return taskWorkTimeLeft;
        }

        public Set<GraphNode> getDependencies() {
            return dependencies;
        }

        public Set<GraphNode> getFollowUps() {
            return followUps;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            GraphNode graphNode = (GraphNode) o;
            return task.equals(graphNode.task);
        }

        @Override
        public int hashCode() {
            return Objects.hash(task);
        }

        @Override
        public String toString() {
            return "GraphNode{" +
                "task=" + task +
                ", taskWorkTimeLeft=" + taskWorkTimeLeft +
                ", dependencies=" + dependencies.stream().map(GraphNode::getTask).collect(toList()) +
                ", followUps=" + followUps.stream().map(GraphNode::getTask).collect(toList()) +
                '}';
        }
    }
}
