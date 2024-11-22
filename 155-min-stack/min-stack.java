class MinStack {
    private int[] realStack;
    private int realPointer;
    private int[] minValueStack;
    private int minValuePointer;

    public MinStack() {
        realStack = new int[15600];
        realPointer = -1;
        minValueStack = new int[1110];
        minValuePointer = -1;
    }

    public void push(int val) {
        realPointer++;
        realStack[realPointer] = val;

        if (minValuePointer == -1 || val <= minValueStack[minValuePointer]) {
            minValuePointer++;
            minValueStack[minValuePointer] = val;
        }
    }

    public void pop() {
        if (realPointer >= 0) {
            if (realStack[realPointer] == minValueStack[minValuePointer]) {
                minValuePointer--;
            }
            realPointer--;
        }
    }

    public int top() {
        if (realPointer < 0) {
            throw new IllegalStateException("Stack is empty");
        }
        return realStack[realPointer];
    }

    public int getMin() {
        if (minValuePointer < 0) {
            throw new IllegalStateException("Stack is empty");
        }
        return minValueStack[minValuePointer];}
}