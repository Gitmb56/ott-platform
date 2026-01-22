import api from './api'

export interface Video {
  id: string
  title: string
  description: string
  thumbnail: string
  duration: string
  url: string
}

export const videoService = {
  async getVideos(): Promise<Video[]> {
    const response = await api.get('/videos')
    return response.data
  },

  async getVideo(id: string): Promise<Video> {
    const response = await api.get(`/videos/${id}`)
    return response.data
  },

  async getEpisodes(seriesId: string): Promise<Video[]> {
    const response = await api.get(`/videos/${seriesId}/episodes`)
    return response.data
  },
}