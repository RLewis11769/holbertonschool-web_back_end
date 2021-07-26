export default function guardrail(mathFunction) {
  // Returns return from function and message in array

  try {
    return [mathFunction(), 'Guardrail was processed'];
  } catch (e) {
    return [`${e.name}: ${e.message}`, 'Guardrail was processed'];
  }
}
