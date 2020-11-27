import java.util.List;

import puzzle.adventofcode.Solution;
import puzzle.adventofcode.year2018.day1.Day1Solution;
import puzzle.adventofcode.year2018.day2.Day2Solution;
import puzzle.adventofcode.year2018.day3.Day3Solution;
import puzzle.adventofcode.year2018.day4.Day4Solution;
import puzzle.adventofcode.year2018.day5.Day5Solution;
import puzzle.adventofcode.year2018.day6.Day6Solution;
import puzzle.adventofcode.year2018.day7.Day7Solution;

public class Main {
    public static void main(String[] args) {
        var solutions = List.of(new Day1Solution(), new Day2Solution(), new Day3Solution(),
            new Day4Solution(), new Day5Solution(), new Day6Solution()/*, new Day7Solution()*/);
        solutions.stream().forEach(Solution::run);
    }
}
