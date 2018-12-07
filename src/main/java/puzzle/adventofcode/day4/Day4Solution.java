package puzzle.adventofcode.day4;

import static java.nio.file.Files.readAllLines;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Comparator;

import puzzle.adventofcode.Solution;

public class Day4Solution implements Solution {

    private Comparator<String> logComparator = LogComparator.INSTANCE;

    @Override
    public void run() {
        try {
            var systemLogs = readAllLines(Path.of("C:/stash/AdventOfCode/src/main/resources/puzzle4a_input.txt"));
            systemLogs.sort(logComparator);
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }

    }
}
