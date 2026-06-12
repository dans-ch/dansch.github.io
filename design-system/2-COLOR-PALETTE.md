# 🎨 Color Palette - DanSch Design System

## Filosofia das Cores

- **Azul Principal:** Confiança, tecnologia, profissionalismo
- **Ciano/Teal:** Inovação, futuro, transformação digital
- **Violeta Suave:** Humanidade, criatividade, conexão
- **Contraste Alto:** Sempre garantir legibilidade (WCAG AA mínimo)

---

## Cores Primárias

### Primary Blue (Marca)

| Nome            | Hex       | RGB                | Uso                             |
| --------------- | --------- | ------------------ | ------------------------------- |
| `--primary-900` | `#1a3a52` | rgb(26, 58, 82)    | Textos importantes, headers     |
| `--primary-800` | `#283E51` | rgb(40, 62, 81)    | Backgrounds escuros             |
| `--primary-700` | `#3a5a73` | rgb(58, 90, 115)   | Hover states                    |
| `--primary-600` | `#4B79A1` | rgb(75, 121, 161)  | **COR PRINCIPAL** - CTAs, links |
| `--primary-500` | `#5d8bb3` | rgb(93, 139, 179)  | Estados ativos                  |
| `--primary-400` | `#7fa3c4` | rgb(127, 163, 196) | Bordas, ícones secundários      |
| `--primary-300` | `#a1bbd5` | rgb(161, 187, 213) | Backgrounds sutis               |
| `--primary-200` | `#c3d3e6` | rgb(195, 211, 230) | Backgrounds claros              |
| `--primary-100` | `#e5ebf2` | rgb(229, 235, 242) | Backgrounds muito claros        |
| `--primary-50`  | `#f0f4f8` | rgb(240, 244, 248) | Background base claro           |

### Innovation Cyan (Inovação)

| Nome         | Hex       | RGB                | Uso                   |
| ------------ | --------- | ------------------ | --------------------- |
| `--cyan-700` | `#0e7490` | rgb(14, 116, 144)  | Textos de destaque    |
| `--cyan-600` | `#0891b2` | rgb(8, 145, 178)   | Links secundários     |
| `--cyan-500` | `#06b6d4` | rgb(6, 182, 212)   | **Destaque inovação** |
| `--cyan-400` | `#22d3ee` | rgb(34, 211, 238)  | Acentos, badges       |
| `--cyan-300` | `#67e8f9` | rgb(103, 232, 249) | Glow effects          |
| `--cyan-100` | `#cffafe` | rgb(207, 250, 254) | Backgrounds           |

### Human Violet (Humanidade)

| Nome           | Hex       | RGB                | Uso                     |
| -------------- | --------- | ------------------ | ----------------------- |
| `--violet-700` | `#6d28d9` | rgb(109, 40, 217)  | Textos especiais        |
| `--violet-600` | `#7c3aed` | rgb(124, 58, 237)  | CTAs secundários        |
| `--violet-500` | `#8b5cf6` | rgb(139, 92, 246)  | **Destaque humanidade** |
| `--violet-400` | `#a78bfa` | rgb(167, 139, 250) | Hover, bordas           |
| `--violet-300` | `#c4b5fd` | rgb(196, 181, 253) | Textos claros em dark   |
| `--violet-100` | `#ede9fe` | rgb(237, 233, 254) | Backgrounds             |

---

## Cores Neutras

| Nome         | Hex       | Uso                         |
| ------------ | --------- | --------------------------- |
| `--gray-900` | `#111827` | Texto principal (dark mode) |
| `--gray-800` | `#1f2937` | Backgrounds escuros         |
| `--gray-700` | `#374151` | Texto secundário escuro     |
| `--gray-600` | `#4b5563` | Texto desabilitado          |
| `--gray-500` | `#6b7280` | Placeholders                |
| `--gray-400` | `#9ca3af` | Bordas, divisores           |
| `--gray-300` | `#d1d5db` | Bordas claras               |
| `--gray-200` | `#e5e7eb` | Backgrounds sutis           |
| `--gray-100` | `#f3f4f6` | Background alternativo      |
| `--gray-50`  | `#f9fafb` | Background base             |
| `--white`    | `#ffffff` | Branco puro                 |

---

## Cores Semânticas

| Nome              | Hex       | Uso                      |
| ----------------- | --------- | ------------------------ |
| `--success`       | `#10b981` | Confirmações, sucesso    |
| `--success-light` | `#d1fae5` | Background sucesso       |
| `--info`          | `#06b6d4` | Informações              |
| `--info-light`    | `#cffafe` | Background info          |
| `--warning`       | `#f59e0b` | ⚠️ Usar com moderação    |
| `--error`         | `#ef4444` | ⚠️ Apenas erros críticos |

> ⚠️ **Nota:** Evitar laranja, amarelo e vermelho exceto em contextos semânticos específicos (erros, alertas críticos).

---

## Gradientes

### Gradiente Principal (Destaque)

```css
--gradient-primary: linear-gradient(135deg, #4b79a1 0%, #283e51 100%);
```

### Gradiente Inovação (CTAs especiais)

```css
--gradient-innovation: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%);
```

### Gradiente Sutil (Backgrounds)

```css
--gradient-subtle: linear-gradient(180deg, #f0f4f8 0%, #ffffff 100%);
```

---

## Regras de Uso

### ✅ Fazer

- Usar `--primary-600` como cor principal de ação
- Aplicar gradientes apenas em **destaques importantes**
- Manter contraste mínimo de 4.5:1 para textos
- Usar cores claras para **destaque** e escuras para **hierarquia secundária**

### ❌ Evitar

- Laranja (#f97316), Amarelo (#eab308), Vermelho (#ef4444) fora de contexto semântico
- Baixo contraste entre texto e fundo
- Gradientes em textos longos
- Múltiplas cores vibrantes competindo na mesma seção
