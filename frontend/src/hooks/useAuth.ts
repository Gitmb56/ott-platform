'use client'

import { useState, useEffect } from 'react'
import { authService, User } from '@/services/auth.service'

export function useAuth() {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      authService.getProfile()
        .then(setUser)
        .catch(() => {
          localStorage.removeItem('token')
        })
        .finally(() => setLoading(false))
    } else {
      setLoading(false)
    }
  }, [])

  const login = async (email: string, password: string) => {
    const { user, token } = await authService.login({ email, password })
    localStorage.setItem('token', token)
    setUser(user)
  }

  const logout = () => {
    authService.logout()
    setUser(null)
  }

  return { user, loading, login, logout }
}