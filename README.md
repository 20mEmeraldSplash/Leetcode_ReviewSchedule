## Python `for` 循环中的 `continue` 语句

在 Python 中，`for` 循环中的 `continue` 语句的作用是跳过当前循环的剩余部分，直接进入下一次循环迭代。这意味着当执行到 `continue` 时，循环中 `continue` 之后的代码将不会执行，而是立即开始下一次循环。

### 例子：

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
