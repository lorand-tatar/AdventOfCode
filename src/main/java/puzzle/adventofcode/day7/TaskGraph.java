package puzzle.adventofcode.day7;

import java.util.Set;

public class TaskGraph {
    private Set<GraphNode> nodes;

    public TaskGraph(Set<GraphNode> nodes) {
        this.nodes = nodes;
    }

    public Set<GraphNode> getNodes() {
        return nodes;
    }

    @Override
    public String toString() {
        return "TaskGraph{" +
                "nodes=" + nodes +
                '}';
    }

    private class GraphNode {
        private Character task;
        private Set<GraphNode> dependencies;
        private Set<GraphNode> followUps;

        public GraphNode(Character task) {
            this.task = task;
        }

        public GraphNode(Character task, Set<GraphNode> dependencies, Set<GraphNode> followUps) {
            this.task = task;
            this.dependencies = dependencies;
            this.followUps = followUps;
        }

        public Character getTask() {
            return task;
        }

        public Set<GraphNode> getDependencies() {
            return dependencies;
        }

        public Set<GraphNode> getFollowUps() {
            return followUps;
        }

        @Override
        public String toString() {
            return "GraphNode{" +
                    "task=" + task +
                    ", dependencies=" + dependencies +
                    ", followUps=" + followUps +
                    '}';
        }
    }
}
