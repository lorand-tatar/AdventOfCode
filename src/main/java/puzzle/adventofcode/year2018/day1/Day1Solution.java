package puzzle.adventofcode.year2018.day1;

import static java.nio.file.Files.readAllLines;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;

import puzzle.adventofcode.Solution;

public class Day1Solution implements Solution {
    @Override
    public void run() {
        var actualValues = new ArrayList<Long>();
        var valueBuckets = new HashSet<Long>();
        try {
            var deltaValues = readAllLines(Path.of("C:/github/AdventOfCode/src/main/resources/puzzle1b_input.txt"));
            System.out.println("Delta array: " + deltaValues);

            /*do {
                deltaValues.stream()
                    .map(Long::valueOf);
            } while (!foundDuplicate);
*/
            actualValues.add(0, 0L);
            var j = 0;
            boolean foundDuplicate = false;
            do {
                var i = 0;
                for (i = j + 1; i < deltaValues.size() + j + 1; ++i) {
                    final long newlyCalculatedCurrentValue = actualValues.get(i - 1) + Long.valueOf(deltaValues.get(i - j - 1));
                    actualValues.add(i, newlyCalculatedCurrentValue);
                    if (valueBuckets.contains(newlyCalculatedCurrentValue)) {
                        foundDuplicate = true;
                        break;
                    }
                    valueBuckets.add(newlyCalculatedCurrentValue);
                }
                j = i - 1;
            } while (!foundDuplicate);
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }
        System.out.println("actual values: " + actualValues);
    }
}
