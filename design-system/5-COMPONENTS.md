# 🧩 Components - DanSch Design System

## Regra de Border Radius

| Tipo de Elemento              | Border Radius        | Variável        |
| ----------------------------- | -------------------- | --------------- |
| **Botões (clicáveis)**        | Totalmente redondo   | `--radius-full` |
| **Cards, Caixas, Containers** | Arredondamento suave | `--radius-xl`   |
| **Inputs de formulário**      | Arredondamento médio | `--radius-md`   |

> ⚠️ **IMPORTANTE:** Todos os botões devem usar `border-radius: var(--radius-full)` para manter consistência visual.

---

## Botões

### Hierarquia de Botões

1. **Primary** - Ação principal (1 por seção)
2. **Secondary** - Ações alternativas
3. **Outline** - Ações terciárias
4. **Ghost** - Links disfarçados de botão

### Especificações

#### Primary Button

```css
.btn-primary {
  background: var(--primary-600);
  color: var(--white);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-full); /* SEMPRE redondo */
  font-weight: var(--font-weight-medium);
  font-size: var(--font-size-base);
  border: none;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: var(--primary-700);
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
```

#### Innovation Button (Gradiente - Uso em Destaques)

```css
.btn-innovation {
  background: var(--gradient-innovation);
  color: var(--white);
  padding: var(--space-3) var(--space-8);
  border-radius: var(--radius-full); /* SEMPRE redondo */
  font-weight: var(--font-weight-bold);
  border: none;
  box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);
  transition: all 0.3s ease;
}

.btn-innovation:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.5);
}
```

#### Outline Button

```css
.btn-outline {
  background: transparent;
  color: var(--primary-600);
  padding: var(--space-3) var(--space-6);
  border: 2px solid var(--primary-600);
  border-radius: var(--radius-full); /* SEMPRE redondo */
  font-weight: var(--font-weight-medium);
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background: var(--primary-600);
  color: var(--white);
}
```

### Tamanhos de Botão

| Tamanho | Padding     | Font Size | Border Radius   |
| ------- | ----------- | --------- | --------------- |
| Small   | `8px 16px`  | 14px      | `--radius-full` |
| Medium  | `12px 24px` | 16px      | `--radius-full` |
| Large   | `16px 32px` | 18px      | `--radius-full` |

---

## Cards

### Card Padrão

```css
.card {
  background: var(--white);
  border-radius: var(--radius-xl); /* Containers usam --radius-xl */
  padding: var(--space-6);
  box-shadow: var(--shadow-md);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
```

### Card de Destaque (Featured)

```css
.card-featured {
  background: var(--gradient-primary);
  color: var(--white);
  border-radius: var(--radius-xl); /* Containers usam --radius-xl */
  padding: var(--space-8);
  box-shadow: var(--shadow-xl);
}
```

### Card com Borda

```css
.card-bordered {
  background: var(--white);
  border: 1px solid var(--gray-200);
  border-radius: var(--radius-xl); /* Containers usam --radius-xl */
  padding: var(--space-6);
}

.card-bordered:hover {
  border-color: var(--primary-400);
}
```

---

## Navegação

### Header Principal

```css
.header {
  background: rgba(31, 41, 55, 0.95);
  backdrop-filter: blur(10px);
  padding: var(--space-4) 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: var(--z-sticky);
  transition: all 0.4s ease;
}

.header.scrolled {
  padding: var(--space-2) 0;
  box-shadow: var(--shadow-lg);
}
```

### Nav Links

```css
.nav-link {
  color: rgba(255, 255, 255, 0.8);
  font-weight: var(--font-weight-medium);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-sm);
  transition: all 0.3s ease;
}

.nav-link:hover,
.nav-link.active {
  color: var(--white);
  background: rgba(255, 255, 255, 0.1);
}
```

---

## Formulários

### Input Padrão

```css
.form-input {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--gray-300);
  border-radius: var(--radius-md);
  font-family: var(--font-family-primary);
  font-size: var(--font-size-base);
  transition: all 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-600);
  box-shadow: 0 0 0 3px rgba(75, 121, 161, 0.15);
}
```

### Label

```css
.form-label {
  display: block;
  font-weight: var(--font-weight-medium);
  color: var(--gray-700);
  margin-bottom: var(--space-2);
  font-size: var(--font-size-sm);
}
```

---

## Badges

### Badge Padrão

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
  border-radius: var(--radius-full);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge-primary {
  background: var(--primary-100);
  color: var(--primary-700);
}

.badge-innovation {
  background: linear-gradient(
    135deg,
    rgba(139, 92, 246, 0.2),
    rgba(6, 182, 212, 0.2)
  );
  color: var(--violet-600);
  border: 1px solid rgba(139, 92, 246, 0.3);
}

.badge-new {
  background: var(--gradient-innovation);
  color: var(--white);
  animation: pulse 2s ease-in-out infinite;
}
```

---

## Accordion

```css
.accordion-button {
  font-weight: var(--font-weight-medium);
  padding: var(--space-4);
  background: var(--white);
  border: none;
  border-radius: var(--radius-md);
}

.accordion-button:not(.collapsed) {
  background: var(--primary-50);
  color: var(--primary-700);
}

.accordion-button:focus {
  box-shadow: 0 0 0 3px rgba(75, 121, 161, 0.15);
}
```

---

## Lista de Itens

```css
.list-item {
  padding: var(--space-4);
  border-bottom: 1px solid var(--gray-200);
  transition: background 0.2s ease;
}

.list-item:hover {
  background: var(--gray-50);
}

.list-item:last-child {
  border-bottom: none;
}
```

---

## Progress Bar

```css
.progress {
  height: 8px;
  background: var(--gray-200);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: var(--gradient-primary);
  border-radius: var(--radius-full);
  transition: width 0.6s ease;
}
```
