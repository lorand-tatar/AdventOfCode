package puzzle.adventofcode.year2018.day4;

import java.time.LocalDateTime;

class LogEntry {

    private LocalDateTime timestamp;
    private MessageType message;
    private Integer guardId;

    LogEntry(LocalDateTime timestamp, MessageType message, Integer guardId) {
        this.timestamp = timestamp;
        this.message = message;
        this.guardId = guardId;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public MessageType getMessage() {
        return message;
    }

    public Integer getGuardId() {
        return guardId;
    }

    public void setGuardId(Integer guardId) {
        this.guardId = guardId;
    }

    @Override
    public String toString() {
        return "LogEntry{" +
                "timestamp=" + timestamp +
                ", message=" + message +
                ", guardId=" + guardId +
                '}';
    }
}
