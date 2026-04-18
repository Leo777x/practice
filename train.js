/* ⭐️ A-TASK (NodeJS)

Shunday 2 parametrli function tuzing, 
hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

// 🌟 MASALANING YECHIMI:
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