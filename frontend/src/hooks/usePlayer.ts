'use client'

import { useState } from 'react'

export function usePlayer(videoId: string) {
  const [isPlaying, setIsPlaying] = useState(false)
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)

  const play = () => setIsPlaying(true)
  const pause = () => setIsPlaying(false)
  const seek = (time: number) => setCurrentTime(time)

  return {
    isPlaying,
    currentTime,
    duration,
    play,
    pause,
    seek,
  }
}