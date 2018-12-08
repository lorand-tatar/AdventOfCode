package puzzle.adventofcode.day4;

import java.time.LocalDateTime;
import java.util.Comparator;

class LogComparator implements Comparator<LogEntry> {
    static final LogComparator INSTANCE = new LogComparator();

    private LogComparator() {
    }

    @Override
    public int compare(LogEntry o1, LogEntry o2) {
        LocalDateTime timestamp1 = o1.getTimestamp();
        LocalDateTime timestamp2 = o2.getTimestamp();
        if (timestamp1.equals(timestamp2)) {
            return 0;
        }
        return timestamp1.isBefore(timestamp2) ? -1 : 1;
    }
}
