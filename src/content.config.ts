import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const weeks = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/weeks' }),
  schema: z.object({
    week: z.number().int().min(1),
    title: z.string(),
    topic: z.string(),
    description: z.string(),
    module: z.string(),
    semester: z.union([z.literal(1), z.literal(2)]),
    exam: z.boolean().default(false),
    // taslak: iskelet var, notlar eksik | hazir: ders notları tamam
    status: z.enum(['taslak', 'hazir']).default('taslak'),
    // Konu/tarih değişikliği olduğunda sayfada uyarı kutusu olarak gösterilir
    changeNote: z.string().default(''),
    tags: z.array(z.string()).default([]),
    objectives: z.array(z.string()).default([]),
    tools: z.array(z.string()).default([]),
    resources: z
      .array(z.object({ title: z.string(), url: z.string().url(), note: z.string().optional() }))
      .default([]),
  }),
});

const announcements = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/announcements' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    pinned: z.boolean().default(false),
    // bilgi | onemli | sinav
    kind: z.enum(['bilgi', 'onemli', 'sinav']).default('bilgi'),
  }),
});

export const collections = { weeks, announcements };
