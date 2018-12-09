package puzzle.adventofcode.day5;

import puzzle.adventofcode.Solution;

import java.io.IOException;
import java.nio.file.Path;

import static java.nio.file.Files.readAllLines;
import static java.nio.file.Files.readString;

public class Day5Solution implements Solution {

    @Override
    public void run() {
        try {
            var originalPolymer = readString(Path.of("C:/Users/Flori/IdeaProjects/AdventOfCode/src/main/resources/puzzle5a_input.txt"));

            
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }
    }

}
