package puzzle.adventofcode.day4;

import java.util.Comparator;

class LogComparator implements Comparator<String> {
    static final Comparator<String> INSTANCE = new LogComparator();

    private LogComparator() {
    }

    @Override
    public int compare(String o1, String o2) {
        return 0;
    }
}
