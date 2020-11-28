package puzzle.adventofcode.year2018;

import java.util.Objects;

public class Coordinate {
    private Integer x;
    private Integer y;

    public Coordinate(Integer x, Integer y) {
        this.x = x;
        this.y = y;
    }

    public Integer getX() {
        return x;
    }

    public Integer getY() {
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
