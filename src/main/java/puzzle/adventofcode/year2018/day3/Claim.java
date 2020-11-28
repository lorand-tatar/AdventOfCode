package puzzle.adventofcode.year2018.day3;

import puzzle.adventofcode.year2018.Coordinate;

class Claim {
    private int id;
    private Coordinate topLeft;
    private Coordinate topRight;
    private Coordinate bottomLeft;
    private Coordinate bottomRight;

    Claim(int id, int topLeftX, int topLeftY, int topRightX, int topRightY, int bottomLeftX, int bottomLeftY, int bottomRightX, int bottomRightY) {
        this.id = id;
        this.topLeft = new Coordinate(topLeftX, topLeftY);
        this.topRight = new Coordinate(topRightX, topRightY);
        this.bottomLeft = new Coordinate(bottomLeftX, bottomLeftY);
        this.bottomRight = new Coordinate(bottomRightX, bottomRightY);
    }

    int getId() {
        return id;
    }

    Coordinate getTopLeft() {
        return topLeft;
    }

    Coordinate getTopRight() {
        return topRight;
    }

    Coordinate getBottomLeft() {
        return bottomLeft;
    }

    Coordinate getBottomRight() {
        return bottomRight;
    }

    @Override
    public String toString() {
        return "Claim{" +
            "id=" + id +
            ", topLeft=" + topLeft +
            ", topRight=" + topRight +
            ", bottomLeft=" + bottomLeft +
            ", bottomRight=" + bottomRight +
            '}';
    }

}
