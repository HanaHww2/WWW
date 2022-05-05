// My solution (2/20 6:05 PM)
function solution(priorities, location) {
  const docArr = [...Array(priorities.length)].map((_, i) => i + 1);
  const printed = [];

  while (priorities.length !== 0) {
    const curPrio = priorities.shift();
    const curDoc = docArr.shift();

    if (curPrio < Math.max(...priorities)) {
      priorities.push(curPrio);
      docArr.push(curDoc);
    } else {
      printed.push(curDoc);
    }
  }

  return printed.indexOf(location + 1) + 1;
}

// 다시 풀기 (5/4)
function solution(priorities, location) {
  const docs = priorities.reduce((arr, p, i) => {
    arr.push({ name: i, priority: p });
    return arr;
  }, []);

  const printArr = [];
  let order = 1;

  while (docs.length) {
    const cur = docs.shift();
    const curPriority = priorities.shift();

    if (curPriority < Math.max(...priorities)) {
      docs.push(cur);
      priorities.push(curPriority);
    } else {
      printArr.push({ ...cur, order: order++ });
    }
  }

  return printArr.find(v => v.name === location).order;
}

// Other's solution
function solution(priorities, location) {
  let answer = 0;
  while (true) {
    if (location === -1) location = priorities.length - 1;

    if (priorities[0] === Math.max(...priorities)) {
      answer++;

      if (location-- === 0) return answer;
      priorities.shift();
      continue;
    }

    location--;
    priorities.push(priorities.shift());
  }
}
