import java.util.List;

import puzzle.adventofcode.Solution;
import puzzle.adventofcode.day1.Day1Solution;
import puzzle.adventofcode.day2.Day2Solution;
import puzzle.adventofcode.day3.Day3Solution;
import puzzle.adventofcode.day4.Day4Solution;
import puzzle.adventofcode.day5.Day5Solution;
import puzzle.adventofcode.day6.Day6Solution;

public class Main {

    public static void main(String[] args) {
        var solutions = List.of(new Day1Solution(), new Day2Solution(), new Day3Solution(),
                new Day4Solution(), new Day5Solution(), new Day6Solution());
        solutions.stream().forEach(Solution::run);
    }
}
