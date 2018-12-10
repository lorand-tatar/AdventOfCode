package puzzle.adventofcode.day6;

import static java.lang.Integer.valueOf;
import static java.lang.Math.abs;
import static java.nio.file.Files.readAllLines;
import static java.util.Comparator.comparing;
import static java.util.Comparator.naturalOrder;
import static java.util.stream.Collectors.toList;

import java.io.IOException;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

import puzzle.adventofcode.Coordinate;
import puzzle.adventofcode.Solution;

public class Day6Solution implements Solution {

    private static int distanceToXY(int finalX, int finalY, Coordinate givenCoordinate) {
        return abs(finalX - givenCoordinate.getX()) + abs(finalY - givenCoordinate.getY());
    }

    @Override
    public void run() {
        try {
            var rawCoordinates = readAllLines(Path.of("C:/stash/AdventOfCode/src/main/resources/puzzle6a_input.txt"));

            final List<Coordinate> coordinates = rawCoordinates.stream()
                .map(coordinate -> coordinate.split(", "))
                .map(coordinateArray -> new Coordinate(valueOf(coordinateArray[0]),
                    valueOf(coordinateArray[1])))
                .collect(toList());

            var minX = coordinates.stream()
                .min(comparing(Coordinate::getX))
                .get().getX();
            var minY = coordinates.stream()
                .min(comparing(Coordinate::getY))
                .get().getY();
            var maxX = coordinates.stream()
                .max(comparing(Coordinate::getX))
                .get().getX();
            var maxY = coordinates.stream()
                .max(comparing(Coordinate::getY))
                .get().getY();

            System.out.println("minx: " + minX + ", maxx: " + maxX + ", miny: " + minY + ", maxy: " + maxY);

            Map<Coordinate, Coordinate> closestGivenCoordinate = determineClosest(minX, minY, maxX, maxY, coordinates);
            final Map.Entry<Coordinate, Long> safestCoordinateAndItsDomainSize = coordinates.stream()
                .filter(givenCoordinate -> givenCoordinate.getX() != minX &&
                    givenCoordinate.getX() != maxX &&
                    givenCoordinate.getY() != minY &&
                    givenCoordinate.getY() != maxY)
                .map(givenInnerCoordinate -> {
                    final long territorySize = closestGivenCoordinate.entrySet().stream()
                        .filter(closestCoordinateEntry -> closestCoordinateEntry.getValue().equals(givenInnerCoordinate))
                        .count();
                    return Map.entry(givenInnerCoordinate, territorySize);
                })
//                .peek(System.out::println)
                .max(comparing(Map.Entry::getValue))
                .get();
            System.out.println("Winner coordinate: " + safestCoordinateAndItsDomainSize.getKey() + ", and its domain size: " + safestCoordinateAndItsDomainSize.getValue());
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }

    }

    private Map<Coordinate, Coordinate> determineClosest(int minX, int minY, int maxX, int maxY, List<Coordinate> givenCoordinates) {
        var closestToCoordinates = new HashMap<Coordinate, Coordinate>();
        for (var x = minX; x <= maxX; ++x) {
            for (var y = minY; y <= maxY; ++y) {
                final int finalX = x;
                final int finalY = y;

                final Stream<Coordinate> minimalDistanceCoordinates = getMinimalDistanceCoordinatesStream(givenCoordinates, finalX, finalY);
                if (minimalDistanceCoordinates.count() == 1) {
                    closestToCoordinates.put(new Coordinate(finalX, finalY), getMinimalDistanceCoordinatesStream(givenCoordinates, finalX, finalY).findFirst().get());
                }
            }
        }
        return closestToCoordinates;
    }

    private Stream<Coordinate> getMinimalDistanceCoordinatesStream(List<Coordinate> givenCoordinates, int finalX, int finalY) {
        return givenCoordinates.stream()
            .filter(givenCoordinate -> distanceToXY(finalX, finalY, givenCoordinate) ==
                givenCoordinates.stream()
                    .map(givenCoordinate2 -> distanceToXY(finalX, finalY, givenCoordinate2))
                    .min(naturalOrder())
                    .get());
    }
}
