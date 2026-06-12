# ✨ Animations - DanSch Design System

## Filosofia

- **Movimento Sutil:** Animações devem guiar, não distrair
- **Propósito:** Cada animação deve ter uma razão (feedback, hierarquia, transição)
- **Performance:** Preferir `transform` e `opacity` (GPU accelerated)

---

## Timing Functions

| Token            | Valor                                    | Uso                  |
| ---------------- | ---------------------------------------- | -------------------- |
| `--ease-default` | `ease`                                   | Padrão geral         |
| `--ease-in`      | `cubic-bezier(0.4, 0, 1, 1)`             | Saída de elementos   |
| `--ease-out`     | `cubic-bezier(0, 0, 0.2, 1)`             | Entrada de elementos |
| `--ease-in-out`  | `cubic-bezier(0.4, 0, 0.2, 1)`           | Transições suaves    |
| `--ease-bounce`  | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` | Efeito bounce sutil  |

---

## Durações

| Token                | Valor    | Uso                      |
| -------------------- | -------- | ------------------------ |
| `--duration-fast`    | `150ms`  | Micro-interações (hover) |
| `--duration-normal`  | `300ms`  | **Padrão** - transições  |
| `--duration-slow`    | `500ms`  | Animações de entrada     |
| `--duration-slower`  | `800ms`  | GSAP ScrollTrigger       |
| `--duration-slowest` | `1000ms` | Animações especiais      |

---

## Transições Padrão

### Hover em Elementos

```css
.transition-default {
  transition: all var(--duration-normal) var(--ease-out);
}

/* Aplicar em: botões, links, cards */
```

### Hover com Elevação

```css
.hover-lift {
  transition:
    transform var(--duration-normal) var(--ease-out),
    box-shadow var(--duration-normal) var(--ease-out);
}

.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
```

### Hover Suave (Apenas opacidade/cor)

```css
.hover-subtle {
  transition:
    opacity var(--duration-fast) var(--ease-out),
    color var(--duration-fast) var(--ease-out);
}
```

---

## GSAP ScrollTrigger

### Configuração Base

```javascript
gsap.registerPlugin(ScrollTrigger);

// Configuração padrão para fade-up
gsap.utils.toArray(".gsap-fade-up").forEach((element) => {
  gsap.fromTo(
    element,
    {
      opacity: 0,
      y: 50,
    },
    {
      opacity: 1,
      y: 0,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: {
        trigger: element,
        start: "top 85%",
        toggleActions: "play none none none",
      },
    },
  );
});
```

### Classes GSAP Disponíveis

| Classe             | Efeito                                      |
| ------------------ | ------------------------------------------- |
| `.gsap-fade-up`    | Fade in + slide up                          |
| `.gsap-fade-left`  | Fade in + slide from left                   |
| `.gsap-fade-right` | Fade in + slide from right                  |
| `.gsap-scale`      | Fade in + scale up                          |
| `.gsap-stagger`    | Aplicar em containers para stagger children |

### Implementação Completa

```javascript
// Fade Up (padrão)
gsap.utils.toArray(".gsap-fade-up").forEach((el) => {
  gsap.fromTo(
    el,
    { opacity: 0, y: 50 },
    {
      opacity: 1,
      y: 0,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: { trigger: el, start: "top 85%" },
    },
  );
});

// Fade Left
gsap.utils.toArray(".gsap-fade-left").forEach((el) => {
  gsap.fromTo(
    el,
    { opacity: 0, x: -50 },
    {
      opacity: 1,
      x: 0,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: { trigger: el, start: "top 85%" },
    },
  );
});

// Fade Right
gsap.utils.toArray(".gsap-fade-right").forEach((el) => {
  gsap.fromTo(
    el,
    { opacity: 0, x: 50 },
    {
      opacity: 1,
      x: 0,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: { trigger: el, start: "top 85%" },
    },
  );
});

// Scale In
gsap.utils.toArray(".gsap-scale").forEach((el) => {
  gsap.fromTo(
    el,
    { opacity: 0, scale: 0.9 },
    {
      opacity: 1,
      scale: 1,
      duration: 0.6,
      ease: "back.out(1.7)",
      scrollTrigger: { trigger: el, start: "top 85%" },
    },
  );
});

// Stagger Children
gsap.utils.toArray(".gsap-stagger").forEach((container) => {
  const children = container.children;
  gsap.fromTo(
    children,
    { opacity: 0, y: 30 },
    {
      opacity: 1,
      y: 0,
      duration: 0.5,
      stagger: 0.1,
      ease: "power2.out",
      scrollTrigger: { trigger: container, start: "top 85%" },
    },
  );
});
```

---

## Keyframes CSS

### Pulse (Badges, alertas)

```css
@keyframes pulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.05);
    opacity: 0.9;
  }
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}
```

### Float (Logos, ícones decorativos)

```css
@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.animate-float {
  animation: float 4s ease-in-out infinite;
}
```

### Glow Pulse (Efeitos de destaque)

```css
@keyframes glow-pulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 0.5;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.8;
  }
}

.animate-glow {
  animation: glow-pulse 3s ease-in-out infinite;
}
```

### Blink Caret (Typewriter)

```css
@keyframes blink-caret {
  0%,
  100% {
    border-color: transparent;
  }
  50% {
    border-color: currentColor;
  }
}

.typewrite .wrap {
  border-right: 0.08em solid;
  animation: blink-caret 0.75s step-end infinite;
}
```

---

## CSS Variables

```css
:root {
  /* Timing Functions */
  --ease-default: ease;
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);

  /* Durations */
  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;
  --duration-slower: 800ms;
  --duration-slowest: 1000ms;
}
```

---

## Regras de Uso

### ✅ Fazer

- Usar `transform` e `opacity` para performance
- Manter durações entre 200-800ms para a maioria das animações
- Aplicar GSAP ScrollTrigger em seções que entram na viewport
- Usar stagger em listas e grids

### ❌ Evitar

- Animações que duram mais de 1s (exceto loops decorativos)
- Animar propriedades como `width`, `height`, `margin` (reflows)
- Múltiplas animações competindo na mesma área
- Animações em elementos muito pequenos
