package puzzle.adventofcode.day3;

import static java.lang.Boolean.FALSE;
import static java.lang.Boolean.TRUE;
import static java.nio.file.Files.readAllLines;
import static java.util.stream.Collectors.toList;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;

import puzzle.adventofcode.Coordinate;
import puzzle.adventofcode.Solution;

public class Day3Solution implements Solution {

    @Override
    public void run() {
        try {
            var rawClaims = readAllLines(Path.of("C:/stash/AdventOfCode/src/main/resources/puzzle3a_input.txt"));
            System.out.println("Raw claims: " + rawClaims);

            List<Claim> compiledClaims = compileRawClaims(rawClaims);

            var claimCoverages = new HashMap<Coordinate, Integer>();
            long coveredArea = 0;
            var claimsUntouched = new HashMap<Integer, Boolean>();
            compiledClaims.stream().forEach(claim -> claimsUntouched.put(claim.getId(), TRUE));
            for (var claim1 : compiledClaims) {
                for (var claim2 : compiledClaims.subList(compiledClaims.indexOf(claim1) + 1, compiledClaims.size())) {
                    for (var x1 = claim1.getTopLeft().getX(); x1 < claim1.getTopRight().getX() + 1; ++x1)
                        for (var y1 = claim1.getTopLeft().getY(); y1 < claim1.getBottomLeft().getY() + 1; ++y1)
                            if (claim2.getTopLeft().getX() <= x1 &&
                                x1 <= claim2.getTopRight().getX() &&
                                claim2.getTopLeft().getY() <= y1 &&
                                y1 <= claim2.getBottomLeft().getY()) {
                                var actualCoordinate = new Coordinate(x1, y1);
                                var actualCoordinateCoverage = Optional.ofNullable(claimCoverages.get(actualCoordinate)).orElse(0);
                                claimCoverages.put(actualCoordinate, ++actualCoordinateCoverage);
                                claimsUntouched.put(claim1.getId(), FALSE);
                                claimsUntouched.put(claim2.getId(), FALSE);
                            }
                }
            }
            coveredArea = claimCoverages.values().stream().filter(coverage -> coverage > 0).count();
            System.out.println("Multiple claims covered area: " + coveredArea);
            var firstUntouchedId = claimsUntouched.entrySet().stream()
                .filter(touchedEntry -> touchedEntry.getValue())
                .findFirst()
                .get()
                .getKey();
            System.out.println("Untouched claim ID: " + firstUntouchedId);
        } catch (IOException e) {
            System.out.println("Can't read file!");
            System.out.println(e);
        }

    }

    private List<Claim> compileRawClaims(List<String> rawClaims) {
        return rawClaims.stream()
            .map(claim -> claim.split(" "))
            .map(this::assembleClaim).collect(toList());
    }

    private Claim assembleClaim(String[] claimElements) {
        var topLeftInfo = Arrays.stream(claimElements[2].substring(0, claimElements[2].lastIndexOf(":")).split(","))
            .map(Integer::valueOf)
            .toArray(Integer[]::new);
        var sizeInfo = Arrays.stream(claimElements[3].split("x"))
            .map(Integer::valueOf)
            .toArray(Integer[]::new);
        int claimId = Integer.valueOf(claimElements[0].substring(1));
        return new Claim(claimId, topLeftInfo[0], topLeftInfo[1],
            topLeftInfo[0] + sizeInfo[0] - 1, topLeftInfo[1],
            topLeftInfo[0], topLeftInfo[1] + sizeInfo[1] - 1,
            topLeftInfo[0] + sizeInfo[0] - 1, topLeftInfo[1] + sizeInfo[1] - 1);
    }
}
