package puzzle.adventofcode.day3;

import java.util.Objects;

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

    static class Coordinate {
        private int x;
        private int y;

        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        int getX() {
            return x;
        }

        int getY() {
            return y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            Coordinate that = (Coordinate) o;
            return x == that.x &&
                y == that.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public String toString() {
            return "<" +
                "x=" + x +
                ", y=" + y +
                '>';
        }
    }
}
