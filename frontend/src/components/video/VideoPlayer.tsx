'use client'

export default function VideoPlayer({ videoId }: { videoId: string }) {
  return (
    <div className="video-player">
      <video controls className="w-full h-auto">
        <source src={`/videos/${videoId}.mp4`} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  )
}