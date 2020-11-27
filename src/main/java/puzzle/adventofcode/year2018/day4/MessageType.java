package puzzle.adventofcode.year2018.day4;

enum MessageType {
    FALLS_ASLEEP,
    WAKES_UP,
    BEGINS_SHIFT;

    static MessageType parse(String message) {
        MessageType type;
        switch (message.charAt(0)) {
            case 'w':
                type = WAKES_UP;
                break;
            case 'f':
                type = FALLS_ASLEEP;
                break;
            case 'G':
                type = BEGINS_SHIFT;
                break;
            default:
                throw new IllegalStateException("Illegal message type found: " + message);
        }
        return type;
    }
}
