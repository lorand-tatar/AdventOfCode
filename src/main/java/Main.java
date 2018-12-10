import puzzle.adventofcode.Solution;
import puzzle.adventofcode.day7.Day7Solution;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        var solutions = List.of(/*new Day1Solution(), new Day2Solution(), new Day3Solution(),
                new Day4Solution(), new Day5Solution(), new Day6Solution(), */ new Day7Solution());
        solutions.stream().forEach(Solution::run);
    }
}
