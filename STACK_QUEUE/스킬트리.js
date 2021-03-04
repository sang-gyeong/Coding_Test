function solution(skill, skill_trees) {
  let answer = 0;
  let target_skills = skill_trees.map(tree => tree.split('')
                                .filter(s=>skill.includes(s[0])).join(''));
  target_skills.forEach(target => {
      if (skill.substring(0, target.length)===target){
          answer++;
      }
  })
  return answer;
}