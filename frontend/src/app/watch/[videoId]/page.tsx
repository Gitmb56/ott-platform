import VideoPlayer from '@/components/video/VideoPlayer'

interface WatchPageProps {
  params: {
    videoId: string
  }
}

export default function Watch({ params }: WatchPageProps) {
  return (
    <div className="min-h-screen bg-black">
      <VideoPlayer videoId={params.videoId} />
    </div>
  )
}