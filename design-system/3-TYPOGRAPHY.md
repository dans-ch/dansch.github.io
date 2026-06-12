# ✒️ Typography - DanSch Design System

## Família de Fontes

### Fonte Principal: System Font Stack

Usa as fontes nativas de cada sistema operacional para melhor performance e compatibilidade universal.

```css
--font-family-primary:
  -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue",
  Arial, sans-serif;
```

**Renderização por sistema:**

- **macOS/iOS:** San Francisco (SF Pro)
- **Windows:** Segoe UI
- **Android:** Roboto
- **Linux:** Liberation Sans / DejaVu Sans
- **Fallback:** Helvetica Neue, Arial

### Fonte Código: System Mono Stack

Para blocos de código e elementos técnicos.

```css
--font-family-mono:
  "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
```

---

## Importação

### ✅ Nenhuma importação necessária!

System fonts são nativas de cada SO - carregamento instantâneo, sem downloads externos.

---

## Escala Tipográfica

### Headings

| Elemento            | Tamanho Desktop | Tamanho Mobile  | Peso | Line Height |
| ------------------- | --------------- | --------------- | ---- | ----------- |
| `h1` / `.display-1` | 3.5rem (56px)   | 2.5rem (40px)   | 700  | 1.2         |
| `h2` / `.display-2` | 2.75rem (44px)  | 2rem (32px)     | 700  | 1.25        |
| `h3` / `.display-3` | 2rem (32px)     | 1.5rem (24px)   | 600  | 1.3         |
| `h4`                | 1.5rem (24px)   | 1.25rem (20px)  | 600  | 1.35        |
| `h5`                | 1.25rem (20px)  | 1.125rem (18px) | 600  | 1.4         |
| `h6`                | 1rem (16px)     | 1rem (16px)     | 600  | 1.4         |

### Body Text

| Classe       | Tamanho         | Peso | Line Height | Uso              |
| ------------ | --------------- | ---- | ----------- | ---------------- |
| `.text-xl`   | 1.25rem (20px)  | 400  | 1.6         | Lead paragraphs  |
| `.text-lg`   | 1.125rem (18px) | 400  | 1.6         | Texto destacado  |
| `.text-base` | 1rem (16px)     | 400  | 1.6         | **Texto padrão** |
| `.text-sm`   | 0.875rem (14px) | 400  | 1.5         | Texto secundário |
| `.text-xs`   | 0.75rem (12px)  | 400  | 1.5         | Captions, labels |

### Pesos Disponíveis

| Peso    | Valor | Uso                        |
| ------- | ----- | -------------------------- |
| Light   | 300   | Textos grandes decorativos |
| Regular | 400   | **Corpo de texto**         |
| Medium  | 500   | Ênfase, subtítulos         |
| Bold    | 700   | **Títulos, CTAs**          |

---

## CSS Variables

```css
:root {
  /* Font Families - System Font Stack */
  --font-family-primary:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue",
    Arial, sans-serif;
  --font-family-mono:
    "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;

  /* Font Sizes */
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2rem;
  --font-size-4xl: 2.75rem;
  --font-size-5xl: 3.5rem;

  /* Font Weights */
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;

  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-snug: 1.35;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.6;

  /* Letter Spacing */
  --letter-spacing-tight: -0.025em;
  --letter-spacing-normal: 0;
  --letter-spacing-wide: 0.025em;
  --letter-spacing-wider: 0.05em;
}
```

---

## Regras de Uso

### ✅ Fazer

- Usar **font-weight: 700** para títulos e CTAs
- Usar **font-weight: 400** para corpo de texto
- Manter line-height de 1.5-1.6 para legibilidade
- Usar `--font-family-mono` para código e dados técnicos

### ❌ Evitar

- Misturar muitos pesos na mesma seção
- Texto menor que 14px para conteúdo principal
- Line-height menor que 1.4 em parágrafos
- Fontes externas que atrasam carregamento
