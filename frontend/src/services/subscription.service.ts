import api from './api'

export interface Subscription {
  id: string
  plan: string
  status: 'active' | 'inactive'
  expiresAt: string
}

export const subscriptionService = {
  async getSubscription(): Promise<Subscription> {
    const response = await api.get('/subscription')
    return response.data
  },

  async subscribe(planId: string): Promise<Subscription> {
    const response = await api.post('/subscription', { planId })
    return response.data
  },

  async cancelSubscription(): Promise<void> {
    await api.delete('/subscription')
  },
}