# 정규표현식

# 1. **정규 표현식의 기초, 메타 문자**

정규 표현식에서 사용하는 메타 문자(meta characters)에는 다음과 같은 것이 있다.

※ 메타 문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다.

```
. ^ $ * + ? { } [ ] \ | ( )
```

정규 표현식에 위 메타 문자를 사용하면 특별한 의미를 갖게 된다.

이제 가장 간단한 정규 표현식부터 시작해 각 메타 문자의 의미와 사용법을 알아보자.

## 1. **문자 클래스 [ ]**

우리가 가장 먼저 살펴볼 메타 문자는 바로 문자 클래스(character class)인 [ ]이다.

문자 클래스로 만들어진 정규식은 `"[ ] 사이의 문자들과 매치"`라는 의미를 갖는다.

※ 문자 클래스를 만드는 메타 문자인 [ ] 사이에는 어떤 문자도 들어갈 수 있다.

- 즉 정규 표현식이 [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"를 뜻한다.

    이해를 돕기 위해 문자열 "a", "before", "dude"가 정규식 [abc]와 어떻게 매치되는지 살펴보자.

    - "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
    - "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
    - "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

- []안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미한다.

    예를 들어 [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일하다.

    다음은 하이픈(-)을 사용한 문자 클래스의 사용 예이다.

    - [a-zA-Z] : 알파벳 모두
    - [0-9] : 숫자

- 문자 클래스([ ]) 안에는 어떤 문자나 메타 문자도 사용할수 있지만 주의해야 할 메타 문자가 1가지 있다.

    **그것은 바로 `^`인데, 문자 클래스 안에 `^` 메타 문자를 사용할 경우에는 반대(not)라는 의미를 갖는다.**

    예를 들어 `[^0-9]`라는 정규 표현식은 숫자가 아닌 문자만 매치된다.

**[자주 사용하는 문자 클래스]**

[0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식이다.

이렇게 자주 사용하는 정규식은 별도의 표기법으로 표현할 수 있다. 다음을 기억해 두자.

- `\d` - 숫자와 매치, [0-9]와 동일한 표현식이다.
- `\D` - 숫자가 아닌 것과 매치, `[^0-9]`와 동일한 표현식이다.
- `\s` - whitespace 문자와 매치, `[ \t\n\r\f\v]`와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
- `\S` - whitespace 문자가 아닌 것과 매치, `[^ \t\n\r\f\v]`와 동일한 표현식이다.
- `\w` - 문자+숫자(alphanumeric)와 매치, `[a-zA-Z0-9_]`와 동일한 표현식이다.
- `\W` - 문자+숫자(alphanumeric)가 아닌 문자와 매치, `[^a-zA-Z0-9_]`와 동일한 표현식이다.

→ 대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.

## 2. **Dot(.)**

**.는 줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치됨을 의미한다.**

(※ 나중에 배우겠지만 정규식을 작성할 때 re.DOTALL 옵션을 주면 \n 문자와도 매치된다.)

다음 정규식을 보자.

```
a.b
```

위 정규식의 의미는 다음과 같다.

**"a + 모든문자 + b"**

즉 a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치된다는 의미이다.

이해를 돕기 위해 문자열 "aab", "a0b", "abc"가 정규식 `a.b`와 어떻게 매치되는지 살펴보자.

- "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 `.`과 일치하므로 정규식과 매치된다.
- "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 `.`과 일치하므로 정규식과 매치된다.
- "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

다음 정규식을 보자.

```
a[.]b
```

이 정규식의 의미는 다음과 같다.

**"a + Dot(.)문자 + b"**

따라서 정규식 `a[.]b`는 "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다.

※ 만약 앞에서 살펴본 문자 클래스([]) 내에 Dot(.) 메타 문자가 사용된다면

이것은 "모든 문자"라는 의미가 아닌 문자 . 그대로를 의미한다. 혼동하지 않도록 주의하자.

## 3. **반복 (*)**

다음 정규식을 보자.

```
ca*t
```

이 정규식에는 반복을 의미하는 `*` 메타 문자가 사용되었다.

여기에서 사용한 `*`은 `*` 바로 앞에 있는 문자 a가 **0부터 무한대로 반복될 수 있다는 의미이다.**

(※ 여기에서 * 메타 문자의 반복 개수가 무한대라고 표현했는데 사실 메모리 제한으로 2억 개 정도만 가능하다고 한다.)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a78339ab-04a2-45db-88fd-5e52b8290f80/_2021-03-05__1.12.37.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a78339ab-04a2-45db-88fd-5e52b8290f80/_2021-03-05__1.12.37.png)

## 4. **반복 (+)**

반복을 나타내는 또 다른 메타 문자로 `+`가 있다. `+`는 **최소 1번 이상 반복될 때 사용한다.**

즉 `*`가 반복 횟수 0부터라면 `+`는 반복 횟수 1부터인 것이다.

다음 정규식을 보자.

```
ca+t
```

위 정규식의 의미는 다음과 같다.

**"c + a(1번 이상 반복) + t"**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5978e99-46b9-417c-b78a-83866d132434/_2021-03-05__1.12.40.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5978e99-46b9-417c-b78a-83866d132434/_2021-03-05__1.12.40.png)

## 5. **반복 ({m,n}, ?)**

여기에서 잠깐 생각해 볼 게 있다. 반복 횟수를 3회만 또는 1회부터 3회까지만으로 제한하고 싶을 수도 있지 않을까?

{ } 메타 문자를 사용하면 반복 횟수를 고정할 수 있다.

**{m, n} 정규식을 사용하면 반복 횟수가 m부터 n까지 매치할 수 있다.**

또한 m 또는 n을 생략할 수도 있다.

**만약 {3,}처럼 사용하면 반복 횟수가 3 이상인 경우이고 {,3}처럼 사용하면 반복 횟수가 3 이하를 의미한다.**

※ {1,}은 +와 동일하고, {0,}은 *와 동일하다.

### 5-**1.** {m}

```
ca{2}t
```

위 정규식의 의미는 다음과 같다.

**"c + a(반드시 2번 반복) + t"**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/471f3d6a-54d8-4cf0-a495-7708d787bbba/_2021-03-05__1.16.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/471f3d6a-54d8-4cf0-a495-7708d787bbba/_2021-03-05__1.16.10.png)

### 5-**2.** {m, n}

```
ca{2,5}t
```

위 정규식의 의미는 다음과 같다:

**"c + a(2~5회 반복) + t"**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6daa8990-6dfb-47e5-8c19-c5935dbc599e/_2021-03-05__1.16.13.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6daa8990-6dfb-47e5-8c19-c5935dbc599e/_2021-03-05__1.16.13.png)

### 5-**3.** `?`

반복은 아니지만 이와 비슷한 개념으로 `?` 이 있다. `?` 메타문자가 의미하는 것은 `{0, 1}` 이다.

다음 정규식을 보자.

```
ab?c
```

위 정규식의 의미는 다음과 같다:

**"a + b(있어도 되고 없어도 된다) + c"**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16386f8a-ea3e-442b-ad14-fa695cbd4d91/_2021-03-05__1.16.17.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16386f8a-ea3e-442b-ad14-fa695cbd4d91/_2021-03-05__1.16.17.png)

즉 b 문자가 있거나 없거나 둘 다 매치되는 경우이다.

``, `+`, `?` 메타 문자는 모두 `{m, n}` 형태로 고쳐 쓰는 것이 가능하지만

가급적 이해하기 쉽고 표현도 간결한 ``, `+`, `?` 메타 문자를 사용하는 것이 좋다.

# 2. **파이썬에서 정규 표현식을 지원하는 re 모듈**

파이썬은 정규 표현식을 지원하기 위해 re(regular expression의 약어) 모듈을 제공한다.

re 모듈은 파이썬을 설치할 때 자동으로 설치되는 기본 라이브러리이다.

```python
import re
```

# 3. **정규식을 이용한 문자열 검색**

이제 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행해 보자. 컴파일된 패턴 객체는 다음과 같은 4가지 메서드를 제공한다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f9f627f3-9179-476c-a5ff-ac96bb6f0ecd/_2021-03-05__2.13.17.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f9f627f3-9179-476c-a5ff-ac96bb6f0ecd/_2021-03-05__2.13.17.png)

match, search는 정규식과 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다. 

(※ match 객체란 정규식의 검색 결과로 돌려주는 객체이다.)

`match`와 `search` 둘 다 비슷한 의미를 가진 듯 하다.

하지만 어감을 좀 더 살려보면 `match`는 "일치하다"와 좀 더 가깝고 `serach`는 수색에 좀 더 가깝다.

- `match`는 매정하다. 처음이 일치하지 않으면 None을 반환한다.
- `search`는 다정하다. 처음이 일치하지 않더라도 전체를 수색해본다.

## 1. **match**

match 메서드는 문자열의 처음부터 정규식과 매치되는지 조사한다. 위 패턴에 match 메서드를 수행해 보자.

```python
result = re.match('[a-z]+', "python")
print(result)

<re.Match object; span=(0, 6), match='python'>
```

"python" 문자열은 `[a-z]+` 정규식에 부합되므로 match 객체를 돌려준다.

```python
result = re.match('[a-z]+', "3 python")
print(result)

None
```

"3 python" 문자열은 처음에 나오는 문자 3이 정규식 `[a-z]+`에 부합되지 않으므로 None을 돌려준다.

match의 결과로 match 객체 또는 None을 돌려주기 때문에 파이썬 정규식 프로그램은 보통 다음과 같은 흐름으로 작성한다.

```python
m = re.match(정규표현식, 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')

```

즉, match의 결과값이 있을 때만 그다음 작업을 수행하겠다는 것이다.

## 2. **search**

이번에는 search 메서드를 수행해 보자.

```python
result = re.search('[a-z]+', "python")
print(result)

<re.Match object; span=(0, 6), match='python'>
```

"python" 문자열에 search 메서드를 수행하면 match 메서드를 수행했을 때와 동일하게 매치된다.

```python
result = re.search('[a-z]+', "3 python")
print(result)

<re.Match object; span=(2, 8), match='python'>
```

"3 python" 문자열의 첫 번째 문자는 "3"이지만

**search는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색하기 때문에 "3" 이후의 "python" 문자열과 매치된다.**

**이렇듯 match 메서드와 search 메서드는 문자열의 처음부터 검색할지의 여부에 따라 다르게 사용해야 한다.**

## 3. **findall**

이번에는 findall 메서드를 수행해 보자.

```python
result = re.findall('[a-z]+', "life is too short")
print(result)
['life', 'is', 'too', 'short']
```

"life is too short" 문자열의 'life', 'is', 'too', 'short' 단어를 각각 `[a-z]+` 정규식과 매치해서 리스트로 돌려준다.

## 4. **finditer**

이번에는 finditer 메서드를 수행해 보자.

```python
result = re.finditer('[a-z]+', "life is too short")
print(result)

<callable_iterator object at 0x01F5E390>

for r in result:
	print(r)

	<re.Match object; span=(0, 4), match='life'>
	<re.Match object; span=(5, 7), match='is'>
	<re.Match object; span=(8, 11), match='too'>
	<re.Match object; span=(12, 17), match='short'>
```

finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다.

반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.

# 4. **match 객체의 메서드**

자, 이제 match 메서드와 search 메서드를 수행한 결과로 돌려준 match 객체에 대해 알아보자.

앞에서 정규식을 사용한 문자열 검색을 수행하면서 아마도 다음과 같은 궁금증이 생겼을 것이다.

- 어떤 문자열이 매치되었는가?
- 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

match 객체의 메서드를 사용하면 이 같은 궁금증을 해결할 수 있다. 다음 표를 보자.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/85d3d53e-5fe4-4035-b903-2b882bc93ed7/_2021-03-05__2.23.07.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/85d3d53e-5fe4-4035-b903-2b882bc93ed7/_2021-03-05__2.23.07.png)

다음 예로 확인해 보자.

```python
# match
m = re.match('[a-z]+', "python")

m.group()
'python'

m.start()
0

m.end()
6

m.span()
(0, 6)
```

예상한 대로 결괏값이 출력되는 것을 확인할 수 있다.

(+) match 메서드를 수행한 결과로 돌려준 match 객체의 start()의 결괏값은 항상 0일 수밖에 없다.

왜냐하면 match 메서드는 항상 문자열의 시작부터 조사하기 때문이다.

만약 search 메서드를 사용했다면 start() 값은 다음과 같이 다르게 나올 것이다.

```python
# search
m = re.search('[a-z]+', "3 python")

m.group()
'python'

m.start()
2

m.end()
8

m.span()
(2, 8)
```

# 5. **컴파일 옵션**

정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.

- **(S)** DOTALL - `.` 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
- **(I)** IGNORECASE - 대소문자에 관계없이 매치할 수 있도록 한다.
- **(M)** MULTILINE - 여러줄과 매치할 수 있도록 한다. (`^`, `$` 메타문자의 사용과 관계가 있는 옵션이다)

→ 옵션을 사용할 때는 `re.DOTALL`처럼 전체 옵션 이름을 써도 되고 `re.S`처럼 약어를 써도 된다.

## 1. **DOTALL, S**

`.` 메타 문자는 줄바꿈 문자(`\n`)를 제외한 모든 문자와 매치되는 규칙이 있다.

만약 `\n` 문자도 포함하여 매치하고 싶다면 `re.DOTALL` 또는 `re.S` 옵션을 사용해 정규식을 컴파일하면 된다.

```python
import re

p = re.compile('a.b')
m = p.match('a\nb')
print(m)

None
```

정규식이 `a.b`인 경우 문자열 `a\nb`는 매치되지 않음을 알 수 있다.

왜냐하면 `\n`은 `.` 메타 문자와 매치되지 않기 때문이다.

`\n` 문자와도 매치되게 하려면 다음과 같이 `re.DOTALL` 옵션을 사용해야 한다.

```python
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

<_sre.SRE_Match object at 0x01FCF3D8>
```

보통 `re.DOTALL` 옵션은 여러 줄로 이루어진 문자열에서 `\n`에 상관없이 검색할 때 많이 사용한다.

## 2. **IGNORECASE, I**

`re.IGNORECASE` 또는 `re.I` 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션이다. 다음 예제를 보자.

```python
p = re.compile('[a-z]', re.I)
p.match('python')
<re.Match object; span=(0, 1), match='p'>

p.match('Python')
<re.Match object; span=(0, 1), match='p'>

p.match('PYTHON')
<re.Match object; span=(0, 1), match='p'>
```

`[a-z]` 정규식은 소문자만을 의미하지만 re.I 옵션으로 대소문자 구별 없이 매치된다.

## 3. **MULTILINE, M**

`re.MULTILINE` 또는 `re.M` 옵션은 조금 후에 설명할 메타 문자인 `^`, `$`와 연관된 옵션이다.

이 메타 문자에 대해 간단히 설명하자면 `^`는 문자열의 처음을 의미하고, `$`는 문자열의 마지막을 의미한다.

(예를 들어 정규식이 `^python`인 경우 문자열의 처음은 항상 python으로 시작해야 매치되고,

만약 정규식이 `python$`이라면 문자열의 마지막은 항상 python으로 끝나야 매치된다는 의미이다.)

```python
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```

정규식 `^python\s\w+`은 python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미이다.

검색할 문자열 data는 여러 줄로 이루어져 있다.

이 스크립트를 실행하면 다음과 같은 결과를 돌려준다.

```
['python one']
```

`^` 메타 문자에 의해 python이라는 문자열을 사용한 첫 번째 줄만 매치된 것이다.

하지만 `^` 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우도 있을 것이다.

이럴 때 사용할 수 있는 옵션이 바로 `re.MULTILINE` 또는 `re.M`이다. 위 코드를 다음과 같이 수정해 보자.

```python
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```

`re.MULTILINE` 옵션으로 인해 `^` 메타 문자가 문자열 전체가 아닌 각 줄의 처음이라는 의미를 갖게 되었다.

이 스크립트를 실행하면 다음과 같은 결과가 출력된다.

```
['python one', 'python two', 'python three']
```

**즉 `re.MULTILINE` 옵션은 `^`, `$` 메타 문자를 문자열의 각 줄마다 적용해 주는 것이다.**

# 6. **백슬래시 문제**

정규 표현식을 파이썬에서 사용할 때 혼란을 주는 요소가 한 가지 있는데, 바로 백슬래시(`\`)이다.

예를 들어 어떤 파일 안에 있는 `"\section"` 문자열을 찾기 위한 정규식을 만든다고 가정해 보자.

```
\section
```

이 정규식은 `\s` 문자가 whitespace로 해석되어 의도한 대로 매치가 이루어지지 않는다.

위 표현은 다음과 동일한 의미이다.

```
[ \t\n\r\f\v]ection
```

의도한 대로 매치하고 싶다면 다음과 같이 변경해야 한다.

```
\\section
```

즉 위 정규식에서 사용한 `\` 문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용하여 이스케이프 처리를 해야 한다.

따라서 위 정규식을 컴파일하려면 다음과 같이 작성해야 한다.

```python
p = re.compile('\\section')
```

그런데 여기에서 또 하나의 문제가 발견된다.

위처럼 정규식을 만들어서 컴파일하면 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라

`\\`이 `\`로 변경되어 `\section`이 전달된다.

결국 정규식 엔진에 `\\` 문자를 전달하려면 파이썬은 `\\\\`처럼 백슬래시를 4개나 사용해야 한다.

```python
p = re.compile('\\\\section')
```

이렇게 해야만 원하는 결과를 얻을 수 있다. 하지만 너무 복잡하지 않은가?

만약 위와 같이 `\`를 사용한 표현이 계속 반복되는 정규식이라면 너무 복잡해서 이해하기 쉽지않을 것이다.

이러한 문제로 인해 파이썬 정규식에는 **Raw String** 규칙이 생겨나게 되었다.

즉, 컴파일해야 하는 정규식이 Raw String임을 알려 줄 수 있도록 파이썬 문법을 만든 것이다. 그 방법은 다음과 같다.

```python
p = re.compile(r'\\section')
```

**위와 같이 정규식 문자열 앞에 r 문자를 삽입하면 이 정규식은 Raw String 규칙에 의하여**

**백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게 된다.**

(※ 만약 백슬래시를 사용하지 않는 정규식이라면 r의 유무에 상관없이 동일한 정규식이 될 것이다.)

# (+) re.compile을 사용하여 컴파일된 패턴 객체 사용하기

 `re.compile`을 사용하여 컴파일된 패턴 객체로 작업을 수행할 수 있다.

보통 한 번 만든 패턴 객체를 여러번 사용해야 할 때는 이 방법을 사용하는 것이 편리하다.

```python
pattern = re.compile('[a-z]+')
result = pattern.match("python")
```

보통 한 번 만든 패턴 객체를 여러번 사용해야 할 때는 이 방법보다 `re.compile`을 사용하는 것이 편하다.

---

# <———강력한 정규 표현식의 세계로———>

# 1. **메타문자**

아직 살펴보지 않은 메타 문자에 대해서 모두 살펴보자.

여기에서 다룰 메타 문자는 앞에서 살펴본 메타 문자와 성격이 조금 다르다.

앞에서 살펴본 `+`, `*`, `[]`, `{}` 등의 메타문자는 매치가 진행될 때 현재 매치되고 있는 문자열의 위치가 변경된다

(보통 소비된다고 표현한다). 하지만 이와 달리 문자열을 소비시키지 않는 메타 문자도 있다.

이번에는 이런 문자열 소비가 없는(zerowidth assertions) 메타 문자에 대해 살펴보자.

## 1. **|**

`|` 메타 문자는 or과 동일한 의미로 사용된다. `A|B`라는 정규식이 있다면 A 또는 B라는 의미가 된다.

```python
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

<re.Match object; span=(0, 4), match='Crow'>
```

## 2. **^**

`^` 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.

앞에서 살펴본 컴파일 옵션 `re.MULTILINE`을 사용할 경우에는 여러 줄의 문자열일 때 각 줄의 처음과 일치하게 된다.

다음 예를 보자.

```python
print(re.search('^Life', 'Life is too short'))
<re.Match object; span=(0, 4), match='Life'>

print(re.search('^Life', 'My Life'))
None
```

`^Life` 정규식은 Life 문자열이 처음에 온 경우에는 매치하지만 처음 위치가 아닌 경우에는 매치되지 않음을 알 수 있다.

## 3. **$**

`$` 메타 문자는 `^` 메타 문자와 반대의 경우이다. 즉 `$`는 문자열의 끝과 매치함을 의미한다.

다음 예를 보자.

```python
print(re.search('short$', 'Life is too short'))
<re.Match object; span=(12, 17), match='short'>

print(re.search('short$', 'Life is too short, you need python'))
None
```

`short$` 정규식은 검색할 문자열이 short로 끝난 경우에는 매치되지만 그 이외의 경우에는 매치되지 않음을 알 수 있다.

(※ ^ 또는 $ 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경우에는 \^, \$ 로 사용하면 된다.)

## 4. **\A**

`\A`는 문자열의 처음과 매치됨을 의미한다.

`^` 메타 문자와 동일한 의미이지만 `re.MULTILINE` 옵션을 사용할 경우에는 다르게 해석된다.

`**re.MULTILINE` 옵션을 사용할 경우 `^`은 각 줄의 문자열의 처음과 매치되지만**

`**\A`는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.**

## 5. **\Z**

`\Z`는 문자열의 끝과 매치됨을 의미한다.

이것 역시 `\A`와 동일하게 `re.MULTILINE` 옵션을 사용할 경우 `$` 메타 문자와는 달리 전체 문자열의 끝과 매치된다.

## 6. **\b**

`\b`는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.

```python
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

<re.Match object; span=(3, 8), match='class'>
```

`\bclass\b` 정규식은 앞뒤가 whitespace로 구분된 class라는 단어와 매치됨을 의미한다.

따라서 no class at all의 class라는 단어와 매치됨을 확인할 수 있다.

```python
print(p.search('the declassified algorithm'))
None
```

위 예의 the declassified algorithm 문자열 안에도 class 문자열이 포함되어 있긴 하지만

whitespace로 구분된 단어가 아니므로 매치되지 않는다.

```python
print(p.search('one subclass is'))
None
```

subclass 문자열 역시 class 앞에 sub 문자열이 더해져 있으므로 매치되지 않음을 알 수 있다.

`\b` 메타 문자를 사용할 때 주의해야 할 점이 있다.

`\b`는 파이썬 리터럴 규칙에 의하면 백 스페이스를 의미하므로 백스페이스가 아닌 단어 구분자임을 알려 주기 해 

`r'\bclass\b'`처럼 Raw string임을 알려주는 기호 r을 반드시 붙여 주어야 한다.

## 7. **\B**

`\B` 메타 문자는 `\b` 메타 문자와 반대의 경우이다. 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다.

```python
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
None

print(p.search('the declassified algorithm'))
<re.Match object; span=(6, 11), match='class'>

print(p.search('one subclass is'))
None
```

class 단어의 앞뒤에 whitespace가 하나라도 있는 경우에는 매치가 안 되는 것을 확인할 수 있다.

# 2. **그루핑****

ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다고 하자. 어떻게 해야할까?

지금까지 공부한 내용으로는 위 정규식을 작성할 수 없다. 이럴 때 필요한 것이 바로 그루핑(Grouping) 이다.

위 경우는 다음처럼 그루핑을 사용하여 작성할 수 있다.

```
(ABC)+
```

그룹을 만들어 주는 메타 문자는 바로 `( )`이다.

```python
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
<re.Match object; span=(0, 9), match='ABCABCABC'>

print(m.group())
ABCABCABC
```

다음 예를 보자.

```python
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
```

`\w+\s+\d+[-]\d+[-]\d+`은 `이름 + " " + 전화번호` 형태의 문자열을 찾는 정규식이다.

그런데 이렇게 매치된 문자열 중에서 이름만 뽑아내고 싶다면 어떻게 해야 할까?

보통 반복되는 문자열을 찾을 때 그룹을 사용하는데,

**그룹을 사용하는 보다 큰 이유는 위에서 볼 수 있듯이**

**매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위해서인 경우가 더 많다.**

위 예에서 만약 ‘이름’ 부분만 뽑아내려 한다면 다음과 같이 할 수 있다.

```python
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

park
```

이름에 해당하는 `\w+` 부분을 그룹 `(\w+)`으로 만들면 match 객체의 group(인덱스) 메서드를 사용하여

그루핑된 부분의 문자열만 뽑아낼 수 있다. group 메서드의 인덱스는 다음과 같은 의미를 갖는다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5d1a0dd-08e4-4893-bc35-3b70f69c584f/_2021-03-05__4.33.24.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5d1a0dd-08e4-4893-bc35-3b70f69c584f/_2021-03-05__4.33.24.png)

다음 예제를 계속해서 보자.

```python
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

010-1234-1234
```

이번에는 전화번호 부분을 추가로 그룹 `(\d+[-]\d+[-]\d+)`로 만들었다.

이렇게 하면 `group(2)`처럼 사용하여 전화번호만 뽑아낼 수 있다.

만약 전화번호 중에서 국번만 뽑아내고 싶으면 어떻게 해야 할까? 다음과 같이 국번 부분을 또 그루핑하면 된다.

```python
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

010
```

위 예에서 볼 수 있듯이 `(\w+)\s+((\d+)[-]\d+[-]\d+)`처럼 그룹을 중첩되게 사용하는 것도 가능하다.

그룹이 중첩되어 있는 경우는 바깥쪽부터 시작하여 안쪽으로 들어갈수록 인덱스가 증가한다.

### 2-1. **그루핑된 문자열 재참조하기**

그룹의 또 하나 좋은 점은 한 번 그루핑한 문자열을 재참조(Backreferences)할 수 있다는 점이다. 다음 예를 보자.

```python
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()

'the the'
```

정규식 `(\b\w+)\s+\1`은 `(그룹) + " " + 그룹과 동일한 단어`와 매치됨을 의미한다.

이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다.

이것을 가능하게 해주는 것이 바로 재참조 메타 문자인 `\1`이다. `\1`은 정규식의 그룹 중 첫 번째 그룹을 가리킨다.

(※ 두 번째 그룹을 참조하려면 \2를 사용하면 된다.)

### 2-2. **그루핑된 문자열에 이름 붙이기**

정규식 안에 그룹이 무척 많아진다고 가정해 보자. 예를 들어 정규식 안에 그룹이 10개 이상만 되어도 매우 혼란스러울 것이다.

거기에 더해 정규식이 수정되면서 그룹이 추가, 삭제되면 그 그룹을 인덱스로 참조한 프로그램도 모두 변경해 주어야 하는 위험도 갖게 된다.

만약 그룹을 인덱스가 아닌 이름(Named Groups)으로 참조할 수 있다면 어떨까? 그렇다면 이런 문제에서 해방되지 않을까?

이러한 이유로 정규식은 그룹을 만들 때 그룹 이름을 지정할 수 있게 했다. 그 방법은 다음과 같다.

```python
(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
```

위 정규식은 앞에서 본 이름과 전화번호를 추출하는 정규식이다. 기존과 달라진 부분은 다음과 같다.

> (\w+) --> (?P<name>\w+)

대단히 복잡해진 것처럼 보이지만 `(\w+)`라는 그룹에 name이라는 이름을 붙인 것에 불과하다.

여기에서 사용한 `(?...)` 표현식은 정규 표현식의 확장 구문이다.

이 확장 구문을 사용하기 시작하면 가독성이 상당히 떨어지긴 하지만 반면에 강력함을 갖게 된다.

그룹에 이름을 지어 주려면 다음과 같은 확장 구문을 사용해야 한다.

```
(?P<그룹명>...)
```

그룹에 이름을 지정하고 참조하는 다음 예를 보자.

```python
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

park
```

위 예에서 볼 수 있듯이 name이라는 그룹 이름으로 참조할 수 있다.

그룹 이름을 사용하면 정규식 안에서 재참조하는 것도 가능하다.

```python
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()

'the the'
```

위 예에서 볼 수 있듯이 재참조할 때에는 `(?P=그룹이름)`이라는 확장 구문을 사용해야 한다.

# 3. **전방 탐색**

정규식에 막 입문한 사람들이 가장 어려워하는 것이 바로 전방 탐색(Lookahead Assertions) 확장 구문이다.

정규식 안에 이 확장 구문을 사용하면 순식간에 암호문처럼 알아보기 어렵게 바뀌기 때문이다.

하지만 이 전방 탐색이 꼭 필요한 경우가 있으며 매우 유용한 경우도 많으니 꼭 알아 두자.

다음 예를 보자.

```python
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

http:
```

정규식 `.+:`과 일치하는 문자열로 http:를 돌려주었다.

만약 http:라는 검색 결과에서 :을 제외하고 출력하려면 어떻게 해야 할까?

위 예는 그나마 간단하지만 훨씬 복잡한 정규식이어서 그루핑은 추가로 할 수 없다는 조건까지 더해진다면 어떻게 해야 할까?

이럴 때 사용할 수 있는 것이 바로 전방 탐색이다.

전방 탐색에는 긍정(Positive)과 부정(Negative)의 2종류가 있고 다음과 같이 표현한다.

- **긍정형 전방 탐색(`(?=...)`)**

    `...` 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

- **부정형 전방 탐색(`(?!...)`)**

    `...`에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

## 3-1. **긍정형 전방 탐색**

긍정형 전방 탐색을 사용하면 http:의 결과를 http로 바꿀 수 있다. 다음 예를 보자.

```python
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

http
```

정규식 중 `:`에 해당하는 부분에 긍정형 전방 탐색 기법을 적용하여 `(?=:)`으로 변경하였다.

이렇게 되면 기존 정규식과 검색에서는 동일한 효과를 발휘하지만 `:` 에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아

(검색에는 포함되지만 검색 결과에는 제외됨) 검색 결과에서는 `:`이 제거된 후 돌려주는 효과가 있다.

자, 이번에는 다음 정규식을 보자.

```
.*[.].*$
```

이 정규식은 `파일 이름 + . + 확장자`를 나타내는 정규식이다.

이 정규식은 foo.bar, autoexec.bat, sendmail.cf 같은 형식의 파일과 매치될 것이다.

이 정규식에 확장자가 "bat인 파일은 제외해야 한다"는 조건을 추가해 보자. 가장 먼저 생각할 수 있는 정규식은 다음과 같다.

```
.*[.][^b].*$
```

이 정규식은 확장자가 b라는 문자로 시작하면 안 된다는 의미이다.

하지만 이 정규식은 foo.bar라는 파일마저 걸러 낸다. 정규식을 다음과 같이 수정해 보자.

```
.*[.]([^b]..|.[^a].|..[^t])$
```

이 정규식은 확장자의 첫 번째 문자가 b가 아니거나 두 번째 문자가 a가 아니거나 세 번째 문자가 t가 아닌 경우를 의미한다.

이 정규식에 의하여 foo.bar는 제외되지 않고 autoexec.bat은 제외되어 만족스러운 결과를 돌려준다.

하지만 이 정규식은 아쉽게도 sendmail.cf처럼 확장자의 문자 개수가 2개인 케이스를 포함하지 못하는 오동작을 하기 시작한다.

따라서 다음과 같이 바꾸어야 한다.

```
.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$
```

확장자의 문자 개수가 2개여도 통과되는 정규식이 만들어졌다. 하지만 정규식은 점점 더 복잡해지고 이해하기 어려워진다.

그런데 여기에서 bat 파일말고 exe 파일도 제외하라는 조건이 추가로 생긴다면 어떻게 될까?

이 모든 조건을 만족하는 정규식을 구현하려면 패턴은 더욱더 복잡해질 것이다.

## 3.2 **부정형 전방 탐색**

이러한 상황의 구원 투수는 바로 부정형 전방 탐색이다. 위 예는 부정형 전방 탐색을 사용하면 다음과 같이 간단하게 처리된다.

```
.*[.](?!bat$).*$
```

확장자가 bat가 아닌 경우에만 통과된다는 의미이다.

bat 문자열이 있는지 조사하는 과정에서 문자열이 소비되지 않으므로 bat가 아니라고 판단되면 그 이후 정규식 매치가 진행된다.

exe 역시 제외하라는 조건이 추가되더라도 다음과 같이 간단히 표현할 수 있다.

```
.*[.](?!bat$|exe$).*$
```

# 4. **문자열 바꾸기**

sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.

다음 예를 보자.

```python
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')

'colour socks and colour shoes'
```

sub 메서드의 첫 번째 매개변수는 "바꿀 문자열(replacement)"이 되고, 두 번째 매개변수는 "대상 문자열"이 된다.

위 예에서 볼 수 있듯이 blue 또는 white 또는 red라는 문자열이 colour라는 문자열로 바뀌는 것을 확인할 수 있다.

**그런데 딱 한 번만 바꾸고 싶은 경우도 있다.**

**이렇게 바꾸기 횟수를 제어하려면 다음과 같이 세 번째 매개변수로 count 값을 넘기면 된다.**

```python
p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'
```

처음 일치하는 blue만 colour라는 문자열로 한 번만 바꾸기가 실행되는 것을 알 수 있다.

### * **sub 메서드와 유사한 subn 메서드**

subn 역시 sub와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있다.

**돌려준 튜플의 첫 번째 요소는 변경된 문자열이고, 두 번째 요소는 바꾸기가 발생한 횟수이다.**

```python
p = re.compile('(blue|white|red)')
p.subn( 'colour', 'blue socks and red shoes')
('colour socks and colour shoes', 2)
```

## 4.1 **sub 메서드 사용 시 참조 구문 사용하기**

sub 메서드를 사용할 때 참조 구문을 사용할 수 있다. 다음 예를 보자.

```python
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

010-1234-1234 park
```

위 예는 `이름 + 전화번호`의 문자열을 `전화번호 + 이름`으로 바꾸는 예이다.

sub의 바꿀 문자열 부분에 `\g<그룹이름>`을 사용하면 정규식의 그룹 이름을 참조할 수 있게 된다.

다음과 같이 그룹 이름 대신 참조 번호를 사용해도 마찬가지 결과를 돌려준다.

```python
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

010-1234-1234 park
```

## 4.2 **sub 메서드의 매개변수로 함수 넣기**

sub 메서드의 첫 번째 매개변수로 함수를 넣을 수도 있다. 다음 예를 보자.

```python
defhexrepl(match):
     value = int(match.group())
return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')

'Call 0xffd2 for printing, 0xc000 for user code.'
```

hexrepl 함수는 match 객체(위에서 숫자에 매치되는)를 입력으로 받아 16진수로 변환하여 돌려주는 함수이다.

sub의 첫 번째 매개변수로 함수를 사용할 경우 해당 함수의 첫 번째 매개변수에는 정규식과 매치된 match 객체가 입력된다.

그리고 매치되는 문자열은 함수의 반환 값으로 바뀌게 된다.

# 5. **Greedy vs Non-Greedy**

정규식에서 Greedy(탐욕스러운)란 어떤 의미일까? 다음 예제를 보자.

```python
s = '<html><head><title>Title</title>'
len(s)
32

print(re.match('<.*>', s).span())
(0, 32)

print(re.match('<.*>', s).group())
<html><head><title>Title</title>
```

`<.*>` 정규식의 매치 결과로 `<html>` 문자열을 돌려주기를 기대했을 것이다.

하지만 * 메타 문자는 매우 탐욕스러워서 매치할 수 있는 최대한의 문자열인 `<html><head><title>Title</title>` 문자열을 모두 소비해 버렸다.

어떻게 하면 이 탐욕스러움을 제한하고 `<html>` 문자열까지만 소비하도록 막을 수 있을까?

**다음과 같이 non-greedy 문자인 `?`를 사용하면 `*`의 탐욕을 제한할 수 있다.**

```python
print(re.match('<.*?>', s).group())

<html>
```

non-greedy 문자인 `?`는 `*?`, `+?`, `??`, `{m,n}?`와 같이 사용할 수 있다.

가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.

## (+) 유용한 메서드 split

이 메서드는 파이썬 문자열의 기본 메서드인 split과 매우 유사하나, 정규식을 처리할 수 있다.

```python
import re

result = re.split('\d', '가나다0나라마8바나나3S')
result = [r for r in result if r]
print(result)

# ['가나다', '나라마', '바나나', 'S']
```

---

### Reference

[https://wikidocs.net/4309#_5](https://wikidocs.net/4309#_5)