# CS50x 2025 – Lecture 0: Scratch

**Course:** CS50x – Introduction to Computer Science  
**Lecture:** 0 – Scratch  
**Theme:** Learning fundamentals of computer science and programming through a visual language (Scratch).  

---

## 1. Course Introduction

- **CS50 is about problem solving**, not just programming.
  - Focus is on *computational thinking*: breaking problems into smaller, logical steps.
  - Programming is a tool for solving problems, not the end goal.

- **Course philosophy:**
  - Everyone starts at different levels — some with no experience at all.
  - Emphasis on patience, persistence, and community.
  - “What ultimately matters in this course is not so much where you end up relative to your classmates, but where you end up relative to yourself when you began.”

- **Mindset:**
  - Growth-oriented.
  - Expect to struggle — it’s normal and part of learning.
  - Learn to *think algorithmically* and *solve problems efficiently*.

---

## 2. Computers and Representation of Information

### Input → Processing → Output
- **Input**: What goes into the computer (keyboard, mouse, camera, files).  
- **Processing**: Computation/logic applied by the program.  
- **Output**: Results returned (text, graphics, sounds, files).

### Binary Numbers
- Computers operate with **bits** (binary digits).
- Each bit = `0` or `1`.
- Larger units:
  - 8 bits = 1 byte
  - 1024 bytes = 1 KB (kilobyte), and so on.

### Number Systems
- **Unary**: Counting with tally marks (|||| = 4).
- **Decimal (Base 10)**: Numbers 0–9 (human default).
- **Binary (Base 2)**: Only 0 and 1 (computer default).
- **Hexadecimal (Base 16)**: Digits 0–9 and A–F, often used in computing.

| System | Base | Symbols          | Example of “10” |
|-------:|:----:|------------------|-----------------|
| Unary  |  1   | marks `||||`     | 2 = `||`        |
| Decimal| 10   | 0–9              | ten             |
| Binary |  2   | 0,1              | two             |
| Hex    | 16   | 0–9, A–F         | sixteen         |

### Text Representation
- **ASCII**: Maps numbers to characters (e.g., 65 = 'A').
- **Unicode**: Extended standard, supports more symbols, languages, emoji.

### Colors & Images
- **RGB color model**:
  - Red, Green, Blue channels (0–255 each).
  - Combined values determine a pixel’s color.
  - Example: (255, 0, 0) = Red.
- **Images** are grids of pixels, each with an RGB value.
- **Video** = sequence of images played rapidly.

#### Pixel Grid (ASCII)

```
[ (255,0,0) | (0,255,0) | (0,0,255) ]
[ (255,255,0) | (255,0,255) | (0,255,255) ]
```

---

## 3. Algorithms

### Definition
- An **algorithm** is a set of step-by-step instructions to solve a problem.

### Example: Finding a Name in a Phone Book
1. **Linear Search**: Check one page at a time. (O(n))
2. **Binary Search**: Open to middle, decide left/right, repeat. (O(log n))

### Efficiency
- Important to consider how long an algorithm takes as input size grows.
- Introduces **Big O Notation** (efficiency classification).

---

## 4. Pseudocode

- **Pseudocode** = writing the steps of an algorithm in plain, structured English.
- Allows reasoning about logic *before* worrying about programming syntax.

**Example:**
```
if number is even
print "Even"
else
print "Odd"
```


---

## 5. Artificial Intelligence (Intro Idea)

- **Hard-coded approach**: writing responses to specific conditions.  
  - E.g., if user says “hi,” program replies “hello.”  
  - Limitation: does not scale for complex interactions.  

- **Modern AI**: uses training on large datasets, not manually coded responses.  
- **Takeaway**: Even complex systems build on simple rules and data representation.

---

## 6. Scratch Programming Language

### Why Scratch?
- Visual, drag-and-drop programming.
- Eliminates syntax errors.
- Lets students focus on *logic* and *problem-solving*.

### Scratch Environment
- **Stage**: Where sprites (characters/objects) perform actions.
- **Sprites**: Characters, images, or objects controlled by blocks.
- **Scripts**: Stack of blocks that define sprite behavior.
- **Coordinate System**:
  - Center = (0,0).
  - x increases right, y increases upward.

### Categories of Blocks
- **Motion**: Move, turn, go to coordinates.
- **Looks**: Say text, switch costume, change size.
- **Sound**: Play sounds/music.
- **Events**: “When green flag clicked,” “When key pressed.”
- **Control**: Loops (`repeat`, `forever`) and conditionals (`if`).
- **Sensing**: Detect mouse, sprite collisions, etc.
- **Operators**: Math, logic, string operations.
- **Variables**: Store and use values.
- **My Blocks**: Create custom functions (abstractions).

---

## 7. Scratch Programming Concepts

### Hello World
- Program says “Hello, world” when the green flag is clicked.

### Hello You
- Ask user for name → capture input → say “Hello, [name]”.

### Variables
- Named containers for data.
- Example: `score = 0` → increase score by 1 when catching an object.

### Loops
- **Repeat n times**: Execute block fixed number of times.
- **Forever**: Continuous loop until program stops.

### Conditionals
- **If/Else** statements to branch logic.
- Example:  
  - If touching edge, bounce.  
  - If score > 10, end game.

### Events
- Respond to user actions or triggers.
- Examples:
  - “When green flag clicked.”
  - “When key [space] pressed.”
  - “When sprite clicked.”

### Functions (Custom Blocks)
- Create reusable sets of instructions.
- Can include **arguments** (inputs).

### Abstraction
- Hiding details by grouping instructions into simpler building blocks.
- Makes programs easier to understand, reuse, and maintain.

---

## 8. Examples Demonstrated

### Simple Programs
- “Say Hello” → one block, direct output.
- “Ask Name” → demonstrates input/output, string concatenation.

### Interactive Demos
- Sprites moving on stage using `move` and `turn` blocks.
- Sprite follows mouse pointer in a loop.

### Games
1. **Oscartime**  
   - Sprite changes costume on mouse-over.  
   - Falling objects to catch or avoid.  
   - Score counter.  

2. **Ivy’s Hardest Game**  
   - Keyboard controls for movement.  
   - Sprite collision detection with walls.  
   - Multiple sprites for enemies/obstacles.  
   - Increasing difficulty.

---

## 9. Key Takeaways

- **Representation**: Computers only understand bits → everything (numbers, text, images, video) is encoded.  
- **Algorithms**: Different approaches can solve the same problem with varying efficiency.  
- **Pseudocode**: Essential tool for planning before coding.  
- **Programming Concepts**: Variables, loops, conditionals, events, functions, abstraction.  
- **Scratch**: A beginner-friendly platform that demonstrates these concepts without worrying about syntax.  
- **Next Steps**: After Scratch, CS50 transitions into C and more advanced, text-based programming.  

---

## 10. Review Checklist

- [ ] Understand binary, ASCII, Unicode, RGB.  
- [ ] Be able to explain input → processing → output.  
- [ ] Explain what an algorithm is, with an example (linear vs binary search).  
- [ ] Write simple pseudocode for everyday problems.  
- [ ] Identify Scratch block categories (motion, looks, control, etc.).  
- [ ] Create variables, loops, conditionals in Scratch.  
- [ ] Use events and sensing to make interactive projects.  
- [ ] Apply abstraction by making custom blocks.  
- [ ] Recall examples: “Hello World,” “Hello You,” “Oscartime,” “Ivy’s Hardest Game.”  

---

