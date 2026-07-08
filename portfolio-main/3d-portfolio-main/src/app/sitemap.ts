import type { MetadataRoute } from "next";
import { config } from "@/data/config";

const routes = ["/", "/resume", "/blogs", "/blogs/achieving-milestone"];

export default function sitemap(): MetadataRoute.Sitemap {
  return routes.map((route) => ({
    url: `${config.site}${route}`,
    lastModified: new Date(),
    changeFrequency: route === "/" ? "weekly" : "monthly",
    priority: route === "/" ? 1 : 0.7,
  }));
}
