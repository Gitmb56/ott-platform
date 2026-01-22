export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001'

export const VIDEO_QUALITIES = ['360p', '480p', '720p', '1080p'] as const

export const SUBSCRIPTION_PLANS = {
  BASIC: 'basic',
  PREMIUM: 'premium',
  VIP: 'vip',
} as const