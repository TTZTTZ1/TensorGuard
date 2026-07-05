# tf.raw_ops.RegexReplace

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RegexReplace](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RegexReplace)

---

Replaces matches of the `pattern` regular expression in `input` with the replacement string provided in `rewrite`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RegexReplace`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RegexReplace)

```
tf.raw_ops.RegexReplace(
    input, pattern, rewrite, replace_global=True, name=None
)
```

It follows the re2 syntax (<https://github.com/google/re2/wiki/Syntax>)

Args:
input: A `Tensor` of type `string`. The text to be processed.
pattern: A `Tensor` of type `string`.
The regular expression to be matched in the `input` strings.
rewrite: A `Tensor` of type `string`.
The rewrite string to be substituted for the `pattern` expression where it is
matched in the `input` strings.
replace\_global: An optional `bool`. Defaults to `True`.
If True, the replacement is global (that is, all matches of the `pattern` regular
expression in each input string are rewritten), otherwise the `rewrite`
substitution is only made for the first `pattern` match.
name: A name for the operation (optional).

Returns:
A `Tensor` of type `string`.