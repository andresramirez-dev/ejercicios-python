// ================================================
// Ejercicios de JavaScript
// Autor: Andrés Ramírez
// Descripción: Ejercicios básicos de JS que se
//              pueden ejecutar en la consola del
//              navegador (F12 → Console)
// ================================================


// ── EJERCICIO 1: Variables y tipos de datos ──
console.log("=== Variables y Tipos de Datos ===");

let nombre = "Andrés";          // texto
let edad = 27;                  // número
let activo = true;              // booleano
let altura = 1.75;              // decimal

console.log("Nombre:", nombre);
console.log("Edad:", edad);
console.log("Activo:", activo);
console.log("Tipo de nombre:", typeof nombre);
console.log("Tipo de edad:", typeof edad);


// ── EJERCICIO 2: Condicionales ──
console.log("\n=== Condicionales ===");

let nota = 82;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 75) {
  console.log("Bueno");
} else if (nota >= 60) {
  console.log("Aprobado");
} else {
  console.log("Reprobado");
}


// ── EJERCICIO 3: Ciclo for ──
console.log("\n=== Ciclo for ===");

let lenguajes = ["Python", "JavaScript", "HTML", "CSS"];

for (let i = 0; i < lenguajes.length; i++) {
  console.log("Lenguaje " + (i + 1) + ":", lenguajes[i]);
}


// ── EJERCICIO 4: Funciones ──
console.log("\n=== Funciones ===");

// Función que saluda a una persona
function saludar(nombre) {
  return "Hola, " + nombre + "! Bienvenido.";
}

// Función que calcula el área de un rectángulo
function calcularArea(base, altura) {
  return base * altura;
}

// Función que verifica si un número es par
function esPar(numero) {
  return numero % 2 === 0;
}

console.log(saludar("Andrés"));
console.log("Área:", calcularArea(5, 3), "m²");
console.log("¿12 es par?", esPar(12));
console.log("¿7 es par?", esPar(7));


// ── EJERCICIO 5: Manipulación de arreglos ──
console.log("\n=== Arreglos ===");

let numeros = [10, 25, 8, 47, 33, 5];

// Encontrar el número mayor
let mayor = numeros[0];
for (let num of numeros) {
  if (num > mayor) {
    mayor = num;
  }
}
console.log("Números:", numeros);
console.log("El mayor es:", mayor);

// Filtrar solo los mayores a 20
let mayoresA20 = numeros.filter(n => n > 20);
console.log("Mayores a 20:", mayoresA20);
