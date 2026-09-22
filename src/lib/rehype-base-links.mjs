/**
 * Markdown içindeki kök göreli bağlantılara (/haftalar/hafta-01 gibi) GitHub Pages
 * base yolunu ekler. Böylece içerik yazarı base'i bilmek zorunda kalmaz.
 */
export default function rehypeBaseLinks({ base = '/' } = {}) {
  const prefix = base.replace(/\/$/, '');
  const visit = (node) => {
    if (node.type === 'element' && (node.tagName === 'a' || node.tagName === 'img')) {
      const key = node.tagName === 'a' ? 'href' : 'src';
      const v = node.properties?.[key];
      if (typeof v === 'string' && v.startsWith('/') && !v.startsWith('//') && prefix && !v.startsWith(prefix + '/')) {
        node.properties[key] = prefix + v;
      }
    }
    node.children?.forEach(visit);
  };
  return (tree) => visit(tree);
}
