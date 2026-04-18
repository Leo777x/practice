/* ⭐️ B-TASK (Nodejs)

Shunday function tuzing, u 1ta string parametrga ega bolsin,
 hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// 🌟 MASALANING YECHIMI:

function countDigits(str) {
  let count = 0;

  for (let i = 0; i < str.length; i++) {
    if (str[i] >= '0' && str[i] <= '9') {
      count++;
    }
  }

  return count;
}

const result = countDigits("ad2a54y79wet0sfgb9");
console.log("result", result)




/* ⭐️ A-TASK (NodeJS)

Shunday 2 parametrli function tuzing, 
hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

// 🌟 MASALANING YECHIMI:

/*
function countLetter(letter, text) {
  let count = 0;

  for (let i = 0; i < text.length; i++) {
    if (text[i] === letter) {
      count++;
    }
  }

  return count;
}
const result = countLetter("e", "engineer");
console.log(result)

*/