import course from '@content/data/course.json';
import modules from '@content/data/modules.json';
import schedule from '@content/data/schedule.json';
import { getCollection, type CollectionEntry } from 'astro:content';

export { course, modules };

export type Module = (typeof modules)[number];
export type Week = CollectionEntry<'weeks'>;
export type ScheduleRow = (typeof schedule.weeks)[number];

/** base path'e duyarlı bağlantı üretir: href('/haftalar') → '/depo/haftalar' */
export function href(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  if (path === '/') return base + '/';
  return base + (path.startsWith('/') ? path : '/' + path);
}

export const weekSlug = (n: number) => `hafta-${String(n).padStart(2, '0')}`;
export const weekHref = (n: number) => href(`/haftalar/${weekSlug(n)}`);

export function moduleOf(id: string): Module {
  const m = modules.find((x) => x.id === id);
  if (!m) throw new Error(`Modül bulunamadı: ${id}`);
  return m;
}

export function scheduleOf(n: number): ScheduleRow | undefined {
  return schedule.weeks.find((r) => r.week === n);
}

export async function getWeeksSorted(): Promise<Week[]> {
  const all = await getCollection('weeks');
  return all.sort((a, b) => a.data.week - b.data.week);
}

const MONTHS = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
const MONTHS_LONG = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];

export function formatDate(iso: string | undefined, long = false): string {
  if (!iso) return '';
  const [y, m, d] = iso.split('-').map(Number);
  if (!y || !m || !d) return '';
  return long ? `${d} ${MONTHS_LONG[m - 1]} ${y}` : `${d} ${MONTHS[m - 1]}`;
}

export function formatDateObj(d: Date): string {
  return `${d.getDate()} ${MONTHS_LONG[d.getMonth()]} ${d.getFullYear()}`;
}

export const STATUS_LABEL: Record<string, string> = {
  normal: '',
  tatil: 'Tatil — ders yok',
  ertelendi: 'Ertelendi',
  sinav: 'Sınav haftası',
};

/** Modül rengi için CSS değişken adı */
export const moduleColorVar = (m: Module) => `var(--mod-${m.color})`;
