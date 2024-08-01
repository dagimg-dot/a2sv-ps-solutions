func isValid(s string) bool {
        if len(s)%2 != 0 {
        return false
    }

    stack := make([]rune, 0)

    open := map[rune]bool{'(': true, '[': true, '{': true}
    paren := map[string]bool{"()": true, "[]": true, "{}": true}

    for _, p := range s {
        if open[p] {
            stack = append(stack, p)
        } else {
            if len(stack) == 0 {
                return false
            }
            lastOpen := stack[len(stack)-1]
            if paren[string(lastOpen)+string(p)] {
                stack = stack[:len(stack)-1] // pop
            } else {
                return false
            }
        }
    }

    return len(stack) == 0
}