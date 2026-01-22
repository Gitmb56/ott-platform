import Link from 'next/link'

interface VideoCardProps {
  id: string
  title: string
  thumbnail: string
  description: string
}

export default function VideoCard({ id, title, thumbnail, description }: VideoCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <img src={thumbnail} alt={title} className="w-full h-48 object-cover" />
      <div className="p-4">
        <h3 className="text-lg font-semibold mb-2">{title}</h3>
        <p className="text-gray-600 text-sm mb-4">{description}</p>
        <Link href={`/watch/${id}`} className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Watch Now
        </Link>
      </div>
    </div>
  )
}