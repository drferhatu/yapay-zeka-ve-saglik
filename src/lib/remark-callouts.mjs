/**
 * Markdown içinde GitHub tarzı uyarı kutuları:
 *   > [!not] ...      → bilgi kutusu
 *   > [!uyari] ...    → uyarı
 *   > [!ornek] ...    → klinik örnek
 *   > [!neden] ...    → "Neden önemli?"
 *   > [!nerede] ...   → "Tıpta nerede kullanılır?"
 *   > [!tanim] ...    → vurgulu tanım
 * İlk satır "[!tur] Başlık" biçiminde olabilir; başlık verilmezse varsayılan kullanılır.
 */
const KINDS = {
  not: { label: 'Not', cls: 'callout-note' },
  uyari: { label: 'Dikkat', cls: 'callout-warn' },
  ornek: { label: 'Klinik örnek', cls: 'callout-example' },
  neden: { label: 'Neden önemli?', cls: 'callout-why' },
  nerede: { label: 'Tıpta nerede kullanılır?', cls: 'callout-where' },
  tanim: { label: 'Tanım', cls: 'callout-def' },
};

const RE = /^\[!(\w+)\]\s*(.*)$/;

function visit(node, fn) {
  if (!node || typeof node !== 'object') return;
  fn(node);
  if (Array.isArray(node.children)) node.children.forEach((c) => visit(c, fn));
}

export default function remarkCallouts() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== 'blockquote' || !node.children?.length) return;
      const first = node.children[0];
      if (first.type !== 'paragraph' || !first.children?.length) return;
      const text = first.children[0];
      if (text.type !== 'text') return;
      const nl = text.value.indexOf('\n');
      const firstLine = nl === -1 ? text.value : text.value.slice(0, nl);
      const m = firstLine.match(RE);
      if (!m) return;
      const kind = KINDS[m[1].toLowerCase()];
      if (!kind) return;
      const title = m[2].trim() || kind.label;
      // ilk satırı kaldır
      text.value = nl === -1 ? '' : text.value.slice(nl + 1);
      if (!text.value) first.children.shift();
      if (!first.children.length) node.children.shift();

      node.data = node.data || {};
      node.data.hName = 'aside';
      node.data.hProperties = { className: ['callout', kind.cls], role: 'note' };
      node.children.unshift({
        type: 'paragraph',
        data: { hName: 'p', hProperties: { className: ['callout-title'] } },
        children: [{ type: 'text', value: title }],
      });
    });
  };
}
