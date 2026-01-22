export interface User {
  id: string
  email: string
  name: string
}

export interface Video {
  id: string
  title: string
  description: string
  thumbnail: string
  duration: string
  url: string
}

export interface Episode extends Video {
  seriesId: string
  episodeNumber: number
}

export interface Subscription {
  id: string
  plan: string
  status: 'active' | 'inactive'
  expiresAt: string
}